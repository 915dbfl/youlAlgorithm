#22.10.31
#토마토
#class3/골드5
#bfs

#시간초과
import sys
from collections import deque

def bfs(h, n, m):
  global answer
  dq = deque([(h, n, m)])

  while dq:
    tmp = dq.popleft()
    cnt = boxes[tmp[0]][tmp[1]][tmp[2]]
    
    for i in range(6):
      nh = tmp[0]+dh[i]
      ny = tmp[1]+dy[i]
      nx = tmp[2]+dx[i]

      if 0<=nh<H and 0<=nx<M and 0<=ny<N:
        if boxes[nh][ny][nx] == 0:
          boxes[nh][ny][nx] = cnt+1
          dq.append((nh, ny, nx))
        elif boxes[nh][ny][nx] > cnt+1:
          boxes[nh][ny][nx] = cnt+1
          dq.append((nh, ny, nx))
        
M, N, H = map(int, sys.stdin.readline().split())

boxes = []

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]

for i in range(H):
  tmp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
  boxes.append(tmp)

for i in range(H):
  for j in range(N):
    for k in range(M):
      if boxes[i][j][k] == 1:
        bfs(i, j, k)

answer = 0
for h in boxes:
  for n in h:
    for m in n:
      if m == 0:
        print(-1)
        exit(0)
    answer = max(answer, max(n))

print(answer-1)

#bfs 다른 풀이
import sys
from collections import deque

def bfs():
  while dq:
    tmp = dq.popleft()
    cnt = boxes[tmp[0]][tmp[1]][tmp[2]]
    
    for i in range(6):
      nh = tmp[0]+dh[i]
      ny = tmp[1]+dy[i]
      nx = tmp[2]+dx[i]

      if 0<=nh<H and 0<=nx<M and 0<=ny<N:
        if boxes[nh][ny][nx] == 0:
          boxes[nh][ny][nx] = cnt+1
          dq.append((nh, ny, nx))
        
M, N, H = map(int, sys.stdin.readline().split())

boxes = []

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]

for i in range(H):
  tmp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
  boxes.append(tmp)

dq = deque()
for i in range(H):
  for j in range(N):
    for k in range(M):
      if boxes[i][j][k] == 1:
        dq.append((i, j, k))

bfs()
answer = 0
for h in boxes:
  for n in h:
    for m in n:
      if m == 0:
        print(-1)
        exit(0)
    answer = max(answer, max(n))

print(answer-1)