#21.10.01
import sys
N = int(input())
dp = [1] * 11
dp[2] = 2
dp[3] = 4
for i in range(N):
  t_case = int(sys.stdin.readline().rstrip())
  for i in range(4, t_case+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
  print(dp[t_case])