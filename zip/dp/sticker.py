#22.11.28
#스티커
#class4/실버1
#dp

#dfs
import sys
sys.setrecursionlimit(10**6)

t = int(sys.stdin.readline())

def dfs(y, x, val):
  global ans
  if x >= n:
    ans = max(ans, val)
    return

  if y == 0:
    visited[y][x] = 1
    dfs(1, x+1, val+sticker[y][x])
    if x > 0 and visited[1][x-1] == 0:
      visited[y][x] = 0
      dfs(1, x, val)
  else:
    visited[y][x] = 1
    dfs(0, x+1, val+sticker[y][x])
    visited[y][x] = 0
    dfs(0, x+1, val)
      
for _ in range(t):
  global ans
  n = int(sys.stdin.readline())

  sticker = []
  for i in range(2):
    sticker.append(list(map(int, sys.stdin.readline().split())))

  visited = [[0]*n, [0]*n]
  ans = 0
  dfs(0, 0, 0)
  print(ans)

#dp
import sys

t = int(sys.stdin.readline())

for _ in range(t):
  n = int(sys.stdin.readline())

  sticker = []
  for _ in range(2):
    sticker.append(list(map(int, sys.stdin.readline().split())))

  if n > 1:
    y, x = 0, 2
    sticker[0][1] += sticker[1][0]
    sticker[1][1] += sticker[0][0]

    while x < n:
      if y == 0:
        sticker[y][x] += max(sticker[1][x-1], sticker[1][x-2])
        y = 1
      else:
        sticker[y][x] += max(sticker[0][x-1], sticker[0][x-2])
        y, x = 0, x+1

  print(max(sticker[0][-1], sticker[1][-1]))