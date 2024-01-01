#22.11.04
#구간 합 구하기
#class3/실버3
#dp: 누적합

import sys

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
dp = [0, nums[0]]

for i in range(1, n):
  dp.append(dp[-1]+nums[i])

for _ in range(m):
  s, e = map(int, sys.stdin.readline().split())
  print(dp[e]-dp[s-1])