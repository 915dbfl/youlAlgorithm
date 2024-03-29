#22.10.19
#미로 탐색
#class3/실버1
# dfs/bfs

#dfs(시간초과)
import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
maze = [sys.stdin.readline().rstrip() for _ in range(N)]

answer = 0

def dfs(y, x, cnt, visited_list):
  global answer
  if y == N-1 and x == M-1:
    answer = max(answer, cnt)
    return
  else:
    if y != 0 and maze[y-1][x] == "1" and [y-1, x] not in visited_list:
      dfs(y-1, x, cnt+1, visited_list + [[y-1, x]])
    if x != 0 and maze[y][x-1] == "1" and [y, x-1] not in visited_list:
      dfs(y, x-1, cnt+1, visited_list + [[y, x-1]])
    if y != N-1 and maze[y+1][x] == "1" and [y+1, x] not in visited_list:
      dfs(y+1, x, cnt+1, visited_list + [[y+1, x]])
    if x != M-1 and maze[y][x+1] == "1" and [y, x+1] not in visited_list:
      dfs(y, x+1, cnt+1, visited_list + [[y, x+1]])

dfs(0, 0, 1, [[0, 0]])
print(answer)

#bfs
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maze = [sys.stdin.readline().rstrip() for _ in range(N)]

def bfs():
  q = deque([[0, 0, 1]])
  visited_lst = [[0 for _ in range(M)] for _ in range(N)]
  visited_lst[0][0] = 1
  answer = N*M

  while q:
    y, x, cnt = q.popleft()
    if y == N-1 and x == M-1:
      answer = min(answer, cnt)
    if y != 0 and maze[y-1][x] == "1" and visited_lst[y-1][x] == 0:
      visited_lst[y-1][x] = 1
      q.append([y-1, x, cnt+1])
    if x != 0 and maze[y][x-1] == "1" and visited_lst[y][x-1] == 0:
      visited_lst[y][x-1] = 1
      q.append([y, x-1, cnt+1])
    if y != N-1 and maze[y+1][x] == "1" and visited_lst[y+1][x] == 0:
      visited_lst[y+1][x] = 1
      q.append([y+1, x, cnt+1])
    if x != M-1 and maze[y][x+1] == "1" and visited_lst[y][x+1] == 0:
      visited_lst[y][x+1] = 1
      q.append([y, x+1, cnt+1])

  print(answer)

bfs()

# bfs 알고리즘(2)
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []

for _ in range(N):
  graph.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  dq = deque([[0, 0]])

  while dq:
    x, y = dq.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        dq.append([nx, ny])

  return graph[N-1][M-1]

print(bfs())