# #22.12.02
# #최소 비용 구하기
# #class4/골드5

#dfs: 시간초과
import sys
from collections import defaultdict
sys.setrecursionlimit(10**4)

def dfs(cur, cost):
  global ans
  costs[cur] = min(costs[cur], cost)
  if cur == e:
    return

  for i, v in dic[cur]:
    if visited[i] == 0 and cost+v < costs[i]:
      visited[i] = 1
      dfs(i, cost+v)
      visited[i] = 0
    
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
dic = defaultdict(list)

for _ in range(m):
  s, e, v = map(int, sys.stdin.readline().split())
  dic[s].append((e, v))

s, e = map(int, sys.stdin.readline().split())
visited = [0]*(n+1)
visited[s] = 1
costs = [n*100000]*(n+1)
dfs(s, 0)
print(costs[e])

#다익스트라
from heapq import heappush, heappop
from collections import defaultdict
import sys

def dijkstra(start):
  q = []
  heappush(q, (0, start))
  distance[start] = 0

  while q:
    dis, cur = heappop(q)

    if distance[cur] < dis:
      continue

    for i in dic[cur]:
      if dis+i[1] < distance[i[0]]:
        distance[i[0]] = dis+i[1]
        heappush(q, (dis+i[1], i[0]))


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
dic = defaultdict(list)

for _ in range(m):
  s, e, v = map(int, sys.stdin.readline().split())
  dic[s].append((e, v))

s, e = map(int, sys.stdin.readline().split())
distance = [n*100000]*(n+1)

dijkstra(s)
print(distance[e])

# 최단경로 알고리즘
# 다익스트라 O(VlogE)
# 벨만 포드(음의 가중치) O(VE)
# 플로이드 워샬 O(N^3)
# bfs(가중치x)