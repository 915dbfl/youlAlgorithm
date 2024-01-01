#22.01.03
#가장 긴 증가하는 부분 수열
import sys
l = int(input())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [1 for i in range(l)]

for i in range(1, l):
  m = 1
  for j in range(0, i):
    if nums[i] > nums[j]:
      if m < dp[j]+1:
        m = dp[j]+1
  dp[i] = m

print(max(dp))