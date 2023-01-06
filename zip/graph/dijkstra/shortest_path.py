#23.01.06
#최단경로
#골드4

import sys
from collections import defaultdict
from heapq import heappop, heappush
INF = sys.maxsize
input = sys.stdin.readline

def dijkstra(start):
  q = [(0, start)]
  distance[start-1] = 0

  while q:
    dis, cur = heappop(q)

    if dis > distance[cur-1]:
      continue

    for i in edges[cur]:
      if dis+i[1] < distance[i[0]-1]:
        distance[i[0]-1] = dis+i[1]
        heappush(q, (dis+i[1], i[0]))

V, E = map(int, input().split())
start = int(input())
edges = defaultdict(list)
distance = [INF]*(V)

for _ in range(E):
  u, v, w = map(int, input().split())
  edges[u].append([v, w])

dijkstra(start)

for i in distance:
  if i < INF:
    print(i)
  else:
    print("INF")