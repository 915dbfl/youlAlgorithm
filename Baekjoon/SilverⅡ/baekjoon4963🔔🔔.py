# 21.01.10
# 4963: 섬의 개수
# bfs, dfs 적용
# 🔔🔔🔔

import sys
sys.setrecursionlimit(10000)

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

def dfs(i, j):
  lst[i][j] = 0
  for k in range(8):
    x = i + dx[k]
    y = j + dy[k]
    if 0 <= x < h and 0 <= y < w and lst[x][y] == 1:
      dfs(x, y)

      

while 1:
  w, h = map(int, sys.stdin.readline().rstrip().split())
  if w == 0 and h == 0:
    break

  lst = []
  for i in range(h):
    lst.append(list(map(int, sys.stdin.readline().rstrip().split())))

  cnt = 0
  for i in range(h):
    for j in range(w):
      if lst[i][j] == 1:
        dfs(i, j)
        cnt += 1

  print(cnt)