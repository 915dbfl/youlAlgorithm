# #22.12.11
# #숨바꼭질3
# #class4/골드5
# #다익스트라

#0-1 bfs
from collections import deque
import sys

def bfs():
  dq = deque([[s, 0]])
  visited = set([s])

  while dq:
    cur, time = dq.popleft()

    if cur == b:
      print(time)
      return
    else:
      if cur < b:
        if cur*2 not in visited:
          dq.appendleft([cur*2, time])
          visited.add(cur*2)
        if cur+1 not in visited:
          dq.append([cur+1, time+1])
          visited.add(cur+1)
      if cur > 0 and cur-1 not in visited:
        dq.append([cur-1, time+1])
        visited.add(cur-1)

s, b = map(int, sys.stdin.readline().split())
if b < s:
  print(s-b)
else:
  bfs()

#dijkstra
import sys
from heapq import heappop, heappush

inf = sys.maxsize # 정수 최댓값

s, b = map(int, sys.stdin.readline().split())
dp = [inf]*100001
heap = []

def dijkstra(s, b):
  if b <= s:
    print(s-b)
    return

  heappush(heap, [0, s])
  while heap:
    t, c = heappop(heap)
    if c == b:
      print(t)
      return
    else:
      for nx in [c*2, c+1, c-1]:
        if 0<= nx <= 100000:
          if nx == c*2 and dp[nx] == inf:
            dp[nx] = t
            heappush(heap, [t, nx])
          elif dp[nx] == inf:
            dp[nx] = t+1
            heappush(heap, [t+1, nx])

dijkstra(s, b)