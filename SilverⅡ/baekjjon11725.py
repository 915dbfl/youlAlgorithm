#21.01.27
#11725: 트리의 부모 찾기

import sys
sys.setrecursionlimit(10**6)

def dfs(n):
  for i in lst[n-1]:
    if parent[i] == 0:
      parent[i] = n
      dfs(i)

N = int(sys.stdin.readline())
lst = [[] for _ in range(N)]
parent = [0 for _ in range(N+1)]

for _ in range(N-1):
  n1, n2 = map(int, sys.stdin.readline().split())
  lst[n1-1].append(n2)
  lst[n2-1].append(n1)

dfs(1)

for i in parent[2:]:
  print(i)