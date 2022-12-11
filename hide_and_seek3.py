#22.12.11
#숨바꼭질3
#class4/골드5
#bfs

#메모리 초과
from collections import deque
import sys

def bfs():
  dq = deque([[s, 0]])

  while dq:
    cur, time = dq.popleft()

    if cur == b:
      print(time)
      return
    else:
      if cur < b:
        dq.append([cur*2, time])
        dq.append([cur+1, time+1])
      if cur > 0:
        dq.append([cur-1, time+1])

s, b = map(int, sys.stdin.readline().split())
bfs()