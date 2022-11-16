#22.11.16
#트리의 지름
#class4/골드2

#bfs/dfs: 시간초과
import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**4)

def dfs(s, c, v):
  for idx, val in dic[c]:
    if visited[idx] == 0:
      visited[idx] = 1
      max_val[idx] = max(max_val[idx], v+val)
      dfs(s, idx, v+val)
      
def bfs(s):
  dq = deque([[s, 0]])

  while dq:
    idx, val = dq.popleft()

    for i, v in dic[idx]:
      if visited[i] == 0:
        visited[i] = 1
        max_val[i] = max(max_val[i], v+val)
        dq.append([i, v+val])

v = int(sys.stdin.readline())
dic = defaultdict(list)
visited = [0]*(v+1)
max_val = [0]*(v+1)
leaves = []

for _ in range(v):
  idx, *lst = map(int, sys.stdin.readline().split())
  if len(lst) == 3:
    leaves.append(idx)
  lst = deque(lst)
  
  while deque(lst):
    tmp = lst.popleft()

    if tmp == -1:
      break
    else:
      dic[idx].append((tmp, lst.popleft()))

for idx in leaves:
  visited[idx] = 1
  bfs(idx)
  visited = [0]*(v+1)

print(max(max_val))