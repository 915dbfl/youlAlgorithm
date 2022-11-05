#22.11.05
#아기 상어
#class3/골드3
#bfs: 최단거리 구하기

import sys
from collections import deque

n = int(sys.stdin.readline())
graph = []
shark = [0, 0]
answer = 0
size = 2
cnt = 0
visited = [[0]*n for _ in range(n)]

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

# 우선순위 높은 먹기
def checkMinPrey(a, b):
  if a[0] > b[0]:
    return b
  elif a[0] == b[0]:
    if a[1] > b[1]:
      return b
    elif a[1] == b[1]:
      if a[2] > b[2]:
        return b
      else:
        return a
    else:
      return a
  else:
    return a

def bfs(y, x, dis):
  dq = deque([[dis, y, x]])
  visited[y][x] = 1
  graph[y][x] = 0
  prey = [n*n+1, n, n]

  while dq:
    d, a, b = dq.popleft()

    if d >= prey[0]:
      continue
    
    for i in range(4):
      ny = a + dy[i]
      nx = b + dx[i]

      if 0<=ny<n and 0<=nx<n and visited[ny][nx] == 0:
        if 0<graph[ny][nx]<size:
          prey = checkMinPrey([d+1, ny, nx], prey)
        elif graph[ny][nx] == 0 or graph[ny][nx] == size:
          visited[ny][nx] = 1
          dq.append([d+1, ny, nx])

  return prey

def findShark():
  for i in range(n):
    for j in range(n):
      if graph[i][j] == 9:
        return [i, j]

for _ in range(n):
  tmp = list(map(int, sys.stdin.readline().split()))
  graph.append(tmp)

# 아기 상어 위치 찾기
shark = findShark()

# 먹이 탐색
while 1:
  prey = bfs(shark[0], shark[1], 0)

  # 먹을 수 있는 먹이가 없을 경우
  if prey[1] == n:
    break
  else:
    # 상어 위치 업데이트
    answer += prey[0]
    shark = [prey[1], prey[2]]
    cnt += 1

    # 상어 크기 업데이트
    if cnt == size:
      size += 1
      cnt = 0

    # 초기화
    visited = [[0]*n for _ in range(n)]

print(answer)