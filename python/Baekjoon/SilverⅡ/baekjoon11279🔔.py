#21.01.19
#11279: 최대 힙
import sys
import heapq

N = int(input())
heap = []

for _ in range(N):
  x = int(sys.stdin.readline())
  if x == 0:
    try:
      print(-1 * heapq.heappop(heap))
    except:
      print(0)

  else:
    heapq.heappush(heap, -x)