#22.10.09
#유기농배추
#class3/실버2
#graph: dfs/bfs

import sys
# sys.setrecursionlimit(10**4)
from collections import deque

t = int(sys.stdin.readline())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# def dfs(y, x):
#   global graph, m, n
#   graph[y][x] = 2

#   for i in range(4):
#     ny = y + dy[i]
#     nx = x + dx[i]

#     if 0<=ny<n and 0 <=nx<m and graph[ny][nx] == 1:
#       dfs(ny, nx)

def bfs(y, x):
  dq = deque([(y, x)])
  graph[y][x] = 2

  while dq:
    a, b = dq.popleft()

    for i in range(4):
      ny = a + dy[i]
      nx = b + dx[i]

      if 0<=ny<n and 0 <=nx<m and graph[ny][nx] == 1:
        graph[ny][nx] = 2
        dq.append((ny, nx))

for _ in range(t):
  global graph, m, n
  m, n, k = map(int, sys.stdin.readline().split())
  graph = [[0]*m for _ in range(n)]
  cnt = 0

  for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    graph[y][x] = 1

  for i in range(n):
    for j in range(m):
      if graph[i][j] == 1:
        cnt += 1
        bfs(i, j)

  print(cnt)