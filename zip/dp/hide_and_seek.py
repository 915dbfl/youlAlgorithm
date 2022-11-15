#22.11.15
#숨바꼭질
#class3/실버1
#dp/bfs

# #dp
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

# #bfs
import sys
from collections import deque

def bfs():
  global n, k
  dq = deque([[n, 0]])
  visited = set()

  while dq:
    val, cnt = dq.popleft()
  
    if val == k:
      print(cnt)
      return
    else:
      if 0<=val-1<=100000 and val-1 not in visited:
        dq.append([val-1, cnt+1])
        visited.add(val-1)
      if 0<=val+1<=100000 and val+1 not in visited:
        visited.add(val+1)
        dq.append([val+1, cnt+1])
      if 0<=val*2<=100000 and val*2 not in visited:
        visited.add(val*2)
        dq.append([val*2, cnt+1])


n, k = map(int, sys.stdin.readline().split())
bfs()