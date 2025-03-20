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

# 직접 gcd 구현하기
"""
최대공약수에 대한 결합법칙 -> gcd(a, b, c) = gcd(gcd(a, b), c)
"""

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

pf_gcd = [0] * (n+1)
sf_gcd = [0] * (n+1)

pf_gcd[0] = nums[0]
for i in range(1, n):
    pf_gcd[i] = gcd(pf_gcd[i-1], nums[i])
sf_gcd[n-1] = nums[n-1]
for i in range(n-2, -1, -1):
    sf_gcd[i] = gcd(sf_gcd[i+1], nums[i])

# 정답 배열
max_gcd = -1
remove = -1
for i in range(n):
    left = pf_gcd[i-1]
    right = sf_gcd[i+1]

    result = gcd(left, right)
    if nums[i] % result == 0:
        continue
    
    if max_gcd < result:
        max_gcd = result
        remove = nums[i]

print(max_gcd, remove)