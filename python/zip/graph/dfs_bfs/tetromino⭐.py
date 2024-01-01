# #22.11.04
# #테트로미노
# #class3/골드4

# # 모든 경우의 수 따지기
import sys

n, m = map(int, sys.stdin.readline().split())
answer = 0
graph = []

for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().split())))

dx = [(0, 1, 2, 3), (0, 0, 0, 0), (0, 0, 0, 1), (0, 1, 2, 2), (0, 1, 1, 1)
  , (0, 1, 1, 1), (0, 0, 1, 2), (0, -1, -1, -1), (0, -1, -1, -2), (0, 0, 1, 1), (0, 0, -1, -1)
    , (0, 1, 1, 2), (0, 1, 1, 2), (0, -1, 0, 1), (0, 0, 0, 1), (0, 0, 0, -1), (0, 0, 1, 1), (0, 0, 1, 2), (0, 0, -1, -2)]
dy = [(0, 0, 0, 0), (0, 1, 2, 3), (0, 1, 2, 2), (0, 0, 0, -1), (0, 0, 1, 2)
  , (0, 0, -1, -2), (0, 1, 1, 1), (0, 0, 1, 2), (0, 0, 1, 1), (0, 1, 1, 2), (0, 1, 1, 2)
  , (0, 0, 1, 1), (0, 0, 1, 0), (0, 1, 1, 1), (0, 1, 2, 1), (0, 1, 2, 1), (0, 1, 1, 0), (0, -1, -1, -1), (0, -1, -1, -1)]

for i in range(n):
  for j in range(m):
    for k in range(19):
      s = 0
      for l in range(4):
        ny = i+dy[k][l]
        nx = j+dx[k][l]

        if 0<=ny<n and 0<=nx<m:
          s += graph[ny][nx]
        else:
          break
      answer = max(answer, s)

print(answer)

#dfs
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

maxValue = 0

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def dfs(y, x, s, t):
  global maxValue

  if t == 4:
    maxValue = max(maxValue, s)
    return

  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]

    if 0<=ny<n and 0<=nx<m and visited[ny][nx] == 0:
      visited[ny][nx] = 1
      dfs(ny, nx, s+graph[ny][nx], t+1)
      visited[ny][nx] = 0

def shapeHats(y, x):
  global maxValue

  for i in range(4):
    tmp = graph[y][x]
    for j in range(3):
      ny = y + dy[(i+j)%4]
      nx = x + dx[(i+j)%4]

      if not (0<=ny<n and 0<=nx<m):
        tmp = 0
        break
      tmp += graph[ny][nx]
    maxValue = max(maxValue, tmp)

for i in range(n):
  for j in range(m):
    visited[i][j] = 1
    dfs(i, j, graph[i][j], 1)
    visited[i][j] = 0

    shapeHats(i, j)

print(maxValue)