#22.11.03
#절댓값 힙
#class3/실버1
#heap

from heapq import heappush, heappop
import sys

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
  tmp = int(sys.stdin.readline())

  if tmp == 0:
    if len(heap) > 0:
      print(heappop(heap)[1])
    else:
      print(0)
  else:
    heappush(heap, (abs(tmp), tmp))