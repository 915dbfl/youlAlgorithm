#22.10.12
#DFS와 BFS
#class3/실버2
#dfs/bfs

import sys
from collections import defaultdict, deque

def dfs(v):
  visited_nodes[v] = 1
  print(v, end= " ")
  for i in dic[v]:
    if visited_nodes[i] == 0:
      dfs(i)
      
def bfs(v):
  dq = deque([v])
  visited_nodes = [0 for i in range(n+1)]       
  visited_nodes[v] = 1   
  while dq:
    i = dq.popleft()
    print(i, end = " ")
    for j in dic[i]:
      if visited_nodes[j] == 0:
        dq.append(j)
        visited_nodes[j] = 1

n, m, v = map(int, sys.stdin.readline().split())
visited_nodes = [0 for i in range(n+1)]

dic = defaultdict(list)

for i in range(m):
  a, b = map(int, sys.stdin.readline().split())
  dic[a].append(b)
  dic[b].append(a)

for i in dic.keys():
  dic[i].sort()

dfs(v)
print()
bfs(v)