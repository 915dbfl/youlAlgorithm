#22.11.21
#트리의 부모 찾기
#class4/실버2
#dfs/bfs

import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**6)

def bfs():
  dq = deque([1])

  while dq:
    tmp = dq.popleft()

    for i in dic[tmp]:
      if visited[i] == 0:
        visited[i] = tmp
        dq.append(i)

def dfs(cur):
  for i in dic[cur]:
    if visited[i] == 0:
      visited[i] = cur
      dfs(i)

n = int(sys.stdin.readline())
dic = defaultdict(list)

for _ in range(n-1):
  a, b = map(int, sys.stdin.readline().split())
  dic[a].append(b)
  dic[b].append(a)

visited = [0]*(n+1)
visited[1] = 1

bfs()

for i in range(2, n+1):
  print(visited[i])