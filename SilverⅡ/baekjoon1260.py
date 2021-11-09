#21.11.01
#시간초과
import sys
from collections import deque
def dfs(v):
  global visit_lst1
  print(v, end=" ")
  visit_lst1[v] = 1
  for i in range(1, N+1):
    if visit_lst1[i] == 0 and graph[v][i] == 1:
      dfs(i)

def bfs(v):
  global visit_lst2
  que = deque()
  que.append(v)
  visit_lst2[v] = 1
  while que:
    temp = que.popleft()
    print(temp, end=" ")
    for i in range(1, N+1):
      if visit_lst2[i] == 0 and graph[temp][i] == 1:
        que.append(i)
        visit_lst2[i] = 1


N, M, V= map(int, sys.stdin.readline().split())
graph = [[0] * (N+1) for _ in range(N+1)]
visit_lst1 = [0 for i in range(N+1)]
visit_lst2 = [0 for i in range(N+1)]

for _ in range(M):
  a, b = map(int, sys.stdin.readline().rstrip().split())
  graph[a][b] = graph[b][a] = 1

dfs(V)
print()
bfs(V)