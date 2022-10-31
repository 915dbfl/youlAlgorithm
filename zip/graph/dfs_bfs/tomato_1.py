#22.10.31
#토마토
#class3/골드5

import sys
from collections import deque

def bfs():
  while dq:
    y, x = dq.popleft()

    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]

      if 0<=ny<n and 0<=nx<m and graph[ny][nx] == 0:
        graph[ny][nx] = graph[y][x]+1
        dq.append((ny, nx))


m, n = map(int, sys.stdin.readline().split())
graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().split())))

dq = deque()
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      dq.append((i, j))

bfs()

answer = 0
for y in graph:
  for x in y:
    if x == 0:
      print(-1)
      exit(0)
  answer = max(answer, max(y))

print(answer-1)