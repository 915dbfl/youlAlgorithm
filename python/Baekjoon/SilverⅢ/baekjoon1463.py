#21.09.30
N = int(input())
dp = [0 for i in range(N+1)]
for i in range(2, N+1):
  dp[i] = 1+dp[i-1]
  if i % 3 == 0:
    dp[i] = min(dp[i], 1 + dp[i//3])
  if i % 2 == 0:
    dp[i] = min(dp[i], 1 + dp[i//2])
print(dp[-1])