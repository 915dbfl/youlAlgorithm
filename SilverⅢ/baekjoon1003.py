#21.10.02
import sys
N = int(input())
dp = [[1, 0] for i in range(41)]
dp[1] = [0, 1]
dp[2] = [1, 1]
for i in range(N):
  case = int(sys.stdin.readline().rstrip())
  for j in range(3, case+1):
    dp[j][0] = dp[j-1][0] + dp[j-2][0]
    dp[j][1] = dp[j-1][1] + dp[j-2][1]
  print(dp[case][0],  dp[case][1])