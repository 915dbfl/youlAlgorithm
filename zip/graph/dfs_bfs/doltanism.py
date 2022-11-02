# #22.11.02
# #적록색약
# #class3/골드5
# #bfs

# #bfs
import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def bfs_b(y, x):
  color = graph[y][x]
  dic[color] += 1
  graph[y][x] = color.lower() if color != "G" else "r"
  dq = deque([(y, x)])

  while dq:
    tmp_y, tmp_x = dq.popleft()

    for i in range(4):
      nx = tmp_x+dx[i]
      ny = tmp_y+dy[i]

      if 0<=nx<n and 0 <=ny<n and graph[ny][nx] == color:
        if color == "G":
          graph[ny][nx] = "r"
        else:
          graph[ny][nx] = color.lower()
        dq.append((ny, nx))

def bfs_d(y, x):
  color = graph[y][x]
  dic[color] += 1
  graph[y][x] = "C"
  dq = deque([(y, x)])

  while dq:
    tmp_y, tmp_x = dq.popleft()

    for i in range(4):
      nx = tmp_x+dx[i]
      ny = tmp_y+dy[i]

      if 0<=nx<n and 0 <=ny<n and graph[ny][nx] == color:
        graph[ny][nx] = "C"
        dq.append((ny, nx))

n = int(input())
graph = []
dic = defaultdict(int)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = []

for _ in range(n):
  graph.append(list(input().rstrip()))

for i in range(n):
  for j in range(n):
    if graph[i][j] == "R" or graph[i][j] == "G" or graph[i][j] == "B":
      bfs_b(i, j)

answer.append(sum(dic.values()))

for i in range(n):
  for j in range(n):
    if graph[i][j] != "C":
      bfs_d(i, j)

answer.append(dic["r"]+dic["b"])
print(answer[0], answer[1])

#dfs
import sys
sys.setrecursionlimit(10**4)

from collections import defaultdict
input = sys.stdin.readline

def dfs(y, x, type):
  color = graph[y][x]
  graph[y][x] = color.lower() if type == 0 else "C"

  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]

    if 0<=ny<n and 0<=nx<n and graph[ny][nx] == color:
      dfs(ny, nx, type)

n = int(input())
graph = []
dic = defaultdict(int)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
a, b = 0, 0

for _ in range(n):
  graph.append(list(input().rstrip()))

for i in range(n):
  for j in range(n):
    if graph[i][j] == "R" or graph[i][j] == "G" or graph[i][j] == "B":
      a += 1
      dfs(i, j, 0)

for i in range(n):
  for j in range(n):
    if graph[i][j] == "g":
      graph[i][j] = "r"

for i in range(n):
  for j in range(n):
    if graph[i][j] != "C":
      b += 1
      dfs(i, j, 1)

print(a, b)