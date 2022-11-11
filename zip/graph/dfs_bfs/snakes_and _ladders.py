#22.11.07
#뱀과 사다리 게임
#class3/골드5
#bfs: 최단거리

import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())
shortcut = [0]*101

def bfs():
  dq = deque([1])
  shortcut[1] = 0

  while dq:
    val = dq.popleft()
    
    for i in range(1, 7):
      if 0<val+i<=100 and shortcut[val+i] >= 0: #방문하지 않은 수
        if shortcut[val+i] == 0: #지름길이 없는 경우
          dq.append(val+i)
        elif shortcut[shortcut[val+i]] >= 0: #지름길이 있는 경우
          shortcut[shortcut[val+i]] = -(-shortcut[val]+1)
          dq.append(shortcut[val+i])
        shortcut[val+i] = -(-shortcut[val]+1)
      
for _ in range(n+m):
  x, y = map(int, sys.stdin.readline().split())
  shortcut[x] = y

bfs()
print(-shortcut[100])

#bfs 다른 풀이
import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())
shortcut = [0]*101
board = [0]*101

def bfs():
  dq = deque([1])

  while dq:
    val = dq.popleft()
    
    for i in range(1, 7):
      new = val+i
      if 0<new<=100:
        if shortcut[new] != 0:
          new = shortcut[new]
          
        if board[new] == 0:
          dq.append(new)
          board[new] = board[val]+1
      
for _ in range(n+m):
  x, y = map(int, sys.stdin.readline().split())
  shortcut[x] = y

print(bfs())