#21.01.25
#11722: 가장 긴 감소하는 부분 수열

import sys
l = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
dp = [1 for _ in range(l)]

for i in range(1, l):
  for j in range(i):
    if A[j] > A[i]:
      if dp[j] + 1 > dp[i]:
        dp[i] = dp[j] + 1

print(max(dp))