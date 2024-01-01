#특정한 최단 경로
#23.01.05
#골드4

#플로이드 워샬: 시간초과
import sys
from itertools import permutations
input = sys.stdin.readline

n, e = map(int, input().split())
graph = [[-1]*(n+1) for _ in range(n+1)]

for _ in range(e):
  a, b, c = map(int, input().split())
  graph[a][b] = c
  graph[b][a] = c

for i in range(1, n+1):
  for j in range(1, n+1):
    for k in range(1, n+1):
      if i == j:
        graph[i][j] = 0
      else:
        if graph[i][k] != -1 and graph[k][j] != -1 and graph[i][j] > graph[i][k] + graph[k][j]:
          graph[i][j] = graph[i][k] + graph[k][j]

print(graph)

lst = list(map(int, input().split()))
answer = sys.maxsize

for case in permutations(lst):
  s, e = 1, 0
  tmp = 0
  for i in case:
    e = i
    tmp += graph[s][e]
    s = i
  tmp += graph[s][n]
  answer = min(answer, tmp)

print(answer)

#다익스트라
import sys
from heapq import heappop, heappush

inpuut = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
  q = [(0, start)]
  tmp = [INF for _ in range(n+1)]
  tmp[start] = 0

  while q:
    dis, cur = heappop(q)

    if tmp[cur] < dis:
      continue

    for i in graph[cur]:
      if dis + i[1] < tmp[i[0]]:
        tmp[i[0]] = dis + i[1]
        heappush(q, (dis+i[1], i[0]))

  return tmp

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

p1, p2 = map(int, input().split())

start = dijkstra(1)
mid1 = dijkstra(p1)
mid2 = dijkstra(p2)

answer = min(start[p1] + mid1[p2] + mid2[n], start[p2] + mid2[p1] + mid1[n])

if answer >= INF:
  print(-1)
else:
  print(answer)