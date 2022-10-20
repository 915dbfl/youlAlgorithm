#22.10.20
#바이러스
#class3/실버3
#dfs/bfs

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n = int(input())
p = int(input())
graph = defaultdict(list)

for _ in range(p):
  s, e = map(int, input().split())
  graph[s].append(e)
  graph[e].append(s)

bfs_nodes = [0 for _ in range(n+1)]
dfs_nodes = [0 for _ in range(n+1)]

def bfs():
  dq = deque([1])
  bfs_nodes[1] = 1
  
  while dq:
    tmp = dq.popleft()

    for i in graph[tmp]:
      if bfs_nodes[i] == 0:
        dq.append(i)
        bfs_nodes[i] = 1
    
  print(bfs_nodes.count(1)-1)

def dfs(cur):
  dfs_nodes[cur] = 1

  for i in graph[cur]:
    if dfs_nodes[i] == 0:
      dfs(i)

dfs(1)
print(dfs_nodes.count(1)-1)