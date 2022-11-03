# #22.11.03
# #경로 찾기
# #class3/실버1
# #dfs, bfs, 플로이드

# #bfs
import sys
from collections import defaultdict, deque

def bfs(k):
  dq = deque(dic[k])
  visited = [0 for _ in range(n)]

  for i in dic[k]:
    visited[i] = 1

  while dq:
    tmp = dq.popleft()
    
    for t in dic[tmp]:
      if visited[t] == 0:
        dic[k].append(t)
        visited[t] = 1
        dq.append(t)

n = int(sys.stdin.readline())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = [["0" for _ in range(n)] for _ in range(n)]
dic = defaultdict(list)

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      dic[i].append(j)

keys = list(dic.keys())
for k in keys:
  bfs(k)

for k in dic.keys():
  for v in dic[k]:
    answer[k][v] = "1"

for l in answer:
  print(" ".join(l))

#bfs 알고리즘 최적화
import sys
from collections import deque

def bfs(i):
  dq = deque([i])

  while dq:
    tmp = dq.popleft()
    
    for k in range(n):
      if graph[tmp][k] == 1 and visited[i][k] == 0:
        visited[i][k] = 1
        dq.append(k)

n = int(sys.stdin.readline())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

for i in range(n):
  bfs(i)

for l in visited:
  print(*l)

#dfs
import sys

def dfs(i):
  for k in range(n):
    if graph[i][k] == 1 and visited[k] == 0:
      visited[k] = 1
      dfs(k)
      
n = int(sys.stdin.readline())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [0]*n

for i in range(n):
  dfs(i)
  print(*visited)
  visited = [0]*n

# 플로이드-와샬
import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for k in range(n):
  for i in range(n):
    for j in range(n):
      if graph[i][k] and graph[k][j]:
        graph[i][j] = 1

for g in graph:
  print(*g)
