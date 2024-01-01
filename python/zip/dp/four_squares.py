#22.11.07
#four squares
#class3/실버3
#dp

#bfs: 최단거리
from collections import deque

def bfs():
  dq = deque([(n, 0)])

  while dq:
    tmp_v, tmp_t = dq.popleft()

    for i in range(int(tmp_v**0.5), 0, -1):
      if tmp_v-i**2 == 0:
        return tmp_t+1
      dq.append((tmp_v-i**2, tmp_t+1))

n = int(input())
print(bfs())

# dp - 최적화
n = int(input())
dp = [0, 1, 2, 3, 1]

for i in range(5, n+1):
  tmp = i
  if i == int(i**0.5)**2:
    dp.append(1)
    continue
  for j in range(1, int(i**0.5)+1):
    tmp = min(tmp, dp[i-j**2]+1)
  dp.append(tmp)
print(dp[n])

# 수학공식

import sys

n = int(sys.stdin.readline())

def getAnswer(n):
  if int(n**0.5) == (n**0.5):
    return 1

  for i in range(1, int(n**0.5)+1):
    if int((n-i**2)**0.5) == (n-i**2)**0.5:
      return 2

  for i in range(1, int(n**0.5)+1):
    for j in range(1, int((n-i**2)**0.5)+1):
      if int((n-i**2-j**2)**0.5) == (n-i**2-j**2)**0.5:
        return 3
  
  return 4

print(getAnswer(n))