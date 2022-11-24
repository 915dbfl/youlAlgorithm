#22.11.24
#a->b
#class4/실버2
#bfs

from collections import deque

#최단 거리를 구하기 = bfs
def bfs(a):
  dq = deque([(a, 1)])

  while dq:
    val, time = dq.popleft()

    if val > b:
      continue
    if val == b:
      print(time)
      return

    dq.append((val*2, time+1))
    dq.append((int(str(val)+"1"), time+1))

  print(-1)
  
a, b = map(int, input().split())
bfs(a)