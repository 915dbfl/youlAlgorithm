#23.01.06
#트리의 지름
#골드4

#dijkstra: 시간초과
import sys
from heapq import heappop, heappush
from collections import defaultdict
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
  q = [(0, start)]
  distance = [INF]*n
  distance[start-1] = 0

  while q:
    dis, cur = heappop(q)

    if dis > distance[cur-1]:
      continue

    for i in edges[cur]:
      tmp = dis+i[1]

      if tmp < distance[i[0]-1]:
        distance[i[0]-1] = tmp
        heappush(q, (tmp, i[0]))

  return distance

n = int(input())
edges = defaultdict(list)
dis = set()

for _ in range(n-1):
  u, v, w = map(int, input().split())
  edges[u].append([v, w])
  edges[v].append([u, w])

answer = 0
for i in range(1, n+1):
  answer = max(answer, max(dijkstra(i)))

print(answer)

#dfs : 시간초과
import sys
from collections import defaultdict
input = sys.stdin.readline

def dfs(cur, diameter):
  global answer
  if answer < diameter:
    answer = diameter

  for n, w in edges[cur]:
    if visited[n] != True:
      visited[n] = True
      dfs(n, diameter + w)
      visited[n] = False

n = int(input())
edges = defaultdict(list)

for _ in range(n-1):
  u, v, w = map(int, input().split())
  edges[u].append([v, w])
  edges[v].append([u, w])

leaves = []
visited = [False]*(n+1)
answer = 0
for i in edges.keys():
  if len(edges[i]) == 1:
    leaves.append(i)

for i in leaves:
  visited[i] = True
  dfs(i, 0)
  visited[i] = False

print(answer)