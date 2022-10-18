#22.10.18
#최소 힙
#class3/실버2
#heap

import sys
from heapq import heappop, heappush

N = int(sys.stdin.readline())
h = []

for _ in range(N):
  num = int(sys.stdin.readline())

  if num == 0:
    try:
      print(heappop(h))
    except:
      print(0)
  else:
    heappush(h, num)