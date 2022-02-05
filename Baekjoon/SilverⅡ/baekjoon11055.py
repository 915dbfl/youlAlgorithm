#21.01.23
#11055: 가장 큰 증가 부분 수열

import sys
s = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
dp = []
for i in A:
  dp.append(i)

for i in range(1, s):
  for j in range(i):
    if A[j] < A[i] and dp[i] < dp[j] + A[i]:
      dp[i] = dp[j] + A[i]

print(max(dp))