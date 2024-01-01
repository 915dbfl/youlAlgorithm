#22.10.18
#최소 힙
#class3/실버2
#heap

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
  x = int(input())

  if x == 0:
    if len(heap) == 0:
      print(0)
    else:
      print(heappop(heap))
  else:
    heappush(heap, x)