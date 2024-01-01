#22.10.09
#피보나치 함수
#class3/실버3
#dp

import sys

t = int(sys.stdin.readline())
dp = [[1, 0], [0, 1]]

for i in range(t):
  n = int(sys.stdin.readline())

  if len(dp) - 1 >= n:
    print(*dp[n])
  else:
    for j in range(len(dp), n+1):
      a = dp[j-1][0] + dp[j-2][0]
      b = dp[j-1][1] + dp[j-2][1]
      dp.append([a, b])
    print(*dp[n])