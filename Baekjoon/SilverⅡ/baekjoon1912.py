# 21.01.05
# 연속합
import sys

n = int(input())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [0 for i in range(n)]
dp[0] = nums[0]

for i in range(1, n):
  if dp[i-1] < 0:
    dp[i] = nums[i]
  else:
    dp[i] = dp[i-1] + nums[i]

print(max(dp))