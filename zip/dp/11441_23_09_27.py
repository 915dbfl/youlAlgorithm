# 합 구하기

# dp
import sys
n = int(input())
lst = list(map(int, input().split()))
dp = [0] * n
dp[0] = lst[0]

for i in range(1, n):
    dp[i] = dp[i-1] + lst[i]

m = int(input())
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    if s <= 1:
        print(dp[e-1])
    else:
        print(dp[e-1] - dp[s-2])