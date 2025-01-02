# 53분
import sys
from math import gcd
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
gcds = [nums[0]]

for i in range(1, n):
    gcds.append(gcd(gcds[-1], nums[i]))

reversed_gcds = [nums[-1]]
for i in range(n-2, -1, -1):
    reversed_gcds.append(gcd(reversed_gcds[-1], nums[i]))

max_gcd = -1
max_k = -1

for i in range(n):
    if i == 0:
        new_gcd = reversed_gcds[n-2]
    elif i == n-1: 
        new_gcd = gcds[n-2]
    else:
        new_gcd = gcd(gcds[i-1], reversed_gcds[n - i - 2])

    if nums[i] % new_gcd != 0:
        if max_gcd < new_gcd:
            max_gcd = new_gcd
            max_k = nums[i]

if max_gcd == -1:
    print(-1)
else:
    print(max_gcd, max_k)