#22.10.16
#숨바꼭질
#class3/실버1
#dp

def getAnswer(n, k):
  for i in range(k+2):
    if i == n:
      dp[i] = 0
    elif i < n:
      dp[i] = n-i
    elif i % 2 == 0:
      dp[i] = min(dp[i-1]+1, dp[i//2]+1)
    else:
      dp[i] = dp[i-1]+1
    
    if i > 0:
      dp[i-1] = min(dp[i]+1, dp[i-1])

N, K = map(int, input().split())

if N >= K:
  print(N-K)
else:
  dp = [0 for _ in range(K+2)]
  getAnswer(N, K)
  print(dp[K])