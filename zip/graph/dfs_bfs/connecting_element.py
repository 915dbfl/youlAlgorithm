#22.11.05
#연결 요소의 개수
#class3/실버2
#bfs/dfs

import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**4)

n, m = map(int,sys.stdin.readline().split())
dic = defaultdict(list)
visited = [0]*(n+1)
cnt = 0

def dfs(c):
  visited[c] = 1

  for i in dic[c]:
    if visited[i] == 0:
      dfs(i)

def bfs(c):
  dq = deque([c])
  visited[c] = 1

  while dq:
    tmp = dq.popleft()

    for i in dic[tmp]:
      if visited[i] == 0:
        visited[i] = 1
        dq.append(i)

for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  dic[a].append(b)
  dic[b].append(a)

for i in range(1, n+1):
  if visited[i] == 0:
    cnt += 1
    bfs(i)

print(cnt)