#22.10.13
#케빈 베이컨의 6단계 법칙
#class3/실버1
#bfs, 플로이드-워셜 알고리즘

#bfs
import sys
from collections import defaultdict, deque

def bfs(i):
  dis = [0 for _ in range(N+1)]
  dq = deque([i])

  while dq:
    v = dq.popleft()
    d = dis[v]
    for j in relations[v]:
      if dis[j] == 0:
        dis[j] = d+1
        dq.append(j)

  return sum(dis)

N, M = map(int, sys.stdin.readline().split())
relations = defaultdict(list)

for i in range(M):
  a, b = map(int, sys.stdin.readline().split())
  relations[a].append(b)
  relations[b].append(a)

answer = []
for i in range(1, N+1):
  answer.append(bfs(i))

print(answer.index(min(answer))+1)

#플로이드 워셜: 모든 노드 간 최단 경로 알아내기

import sys

N, M = map(int, sys.stdin.readline().split())
graph = [[N for _ in range(N)] for _ in range(N)]

for i in range(M):
  a, b = map(int, sys.stdin.readline().split())
  graph[a-1][b-1] = 1
  graph[b-1][a-1] = 1
    
for i in range(N):
  for j in range(N):
    for k in range(N):
      if j == k:
        graph[j][k] = 0
      else:
        graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
                
answer = []
for row in graph:
  answer.append(sum(row))
print(answer.index(min(answer))+1)