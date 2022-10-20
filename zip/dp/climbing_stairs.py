#22.10.20
#계단 오르기
#class3/실버3
#dp

import sys
input = sys.stdin.readline

N = int(input())
values = [int(input()) for _ in range(N)]

dp = [0 for _ in range(N)]
dp[0] = values[0]

for i in range(N):
  if 0 < i < 2:
    dp[i] = dp[i-1] + values[i]
  elif i >= 2:
    dp[i] = max(dp[i-2]+values[i], dp[i-3]+values[i-1]+values[i])

print(dp[-1])