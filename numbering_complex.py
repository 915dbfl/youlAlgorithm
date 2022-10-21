#22.10.21
#단지번호붙이기
#class3/실버1
#bfs/dfs

#bfs
import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
  dq = deque([[i, j]])
  graph[i][j] = 2
  house = 1

  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  while dq:
    i, j= dq.popleft()

    for k in range(4):
      nx = i+dx[k]
      ny = j+dy[k]

      if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 1:
        dq.append([nx, ny])
        graph[nx][ny] = 2
        house += 1

  complexes.append(house)

n = int(input())
graph = []

for _ in range(n):
  graph.append(list(map(int, input().rstrip())))

cnt = 0
complexes = []

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      cnt += 1
      bfs(i, j)

print(cnt)

for i in sorted(complexes):
  print(i)

#dfs
import sys
input = sys.stdin.readline

def dfs(i, j):
  graph[i][j] = 2
  house = 1

  for k in range(4):
    nx = i+dx[k]
    ny = j+dy[k]

    if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 1:
      house += dfs(nx, ny)
  return house

n = int(input())
graph = []

for _ in range(n):
  graph.append(list(map(int, input().rstrip())))

cnt = 0
complexes = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      cnt += 1
      complexes.append(dfs(i, j))

print(cnt)

for i in sorted(complexes):
  print(i)