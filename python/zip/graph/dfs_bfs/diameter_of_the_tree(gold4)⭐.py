#23.01.06
#트리의 지름
#골드4

#dijkstra: 시간초과(O(N^2logN))
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
leaves = []
for i in edges.keys():
  if len(edges[i]) == 1:
    leaves.append(i)
  
for i in leaves:
  answer = max(answer, max(dijkstra(i)))

print(answer)

#dfs(재귀): 시간초과
#dfs(스택): 통과(O(N^2))
import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def dfs(start):
  global answer
  visited = [0]*(N+1)
  need_visited = deque([[start, 0]])
  visited[start] = 1

  while need_visited:
    cur, weight = need_visited.pop()
    if answer < weight:
      answer = weight

    for n, w in dic[cur]:
      if visited[n] == 0:
        visited[n] = 1
        need_visited.append([n, weight+w])

N = int(input())
dic = defaultdict(list)

for _ in range(N-1):
  u, v, w = map(int, input().split())
  dic[u].append((v, w))
  dic[v].append((u, w))

leaves = []
for i in dic.keys():
  if len(dic[i]) == 1:
    leaves.append(i)

answer = 0
for i in leaves:
  dfs(i)
print(answer)

# bfs: 통과(O(N^2))
import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def bfs(start):
  global answer
  q = deque([[start, 0]])
  visited = [0] * (N+1)
  visited[start] = 1

  while q:
    cur, weight = q.popleft()
    if answer < weight:
      answer = weight
    
    for n, w in dic[cur]:
      if visited[n] == 0:
        visited[n] = 1
        q.append([n, weight + w])

N = int(input())
dic = defaultdict(list)

for _ in range(N-1):
  u, v, w = map(int, input().split())
  dic[u].append((v, w))
  dic[v].append((u, w))

leaves = []
for i in dic.keys():
  if len(dic[i]) == 1:
    leaves.append(i)

answer = 0
for i in leaves:
  bfs(i)
print(answer)