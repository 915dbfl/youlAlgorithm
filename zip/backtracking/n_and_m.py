# #22.11.17
# #n과 m(2)
# #class4/실버3

#combination 모듈 사용하기
from itertools import combinations

n, m = map(int, input().split())

lst = [i for i in range(1, n+1)]

for case in combinations(lst, m):
  print(*case)

#백트래킹
def dfs(lst, cur):
  global n, m
  if len(lst) == m:
    print(*lst)
    return
  else:
    for j in range(cur+1, n+1):
      if visited[j] == 0:
        visited[j] = 1
        dfs(lst+[j], j)
        visited[j] = 0

n, m = map(int, input().split())

lst = [i for i in range(1, n+1)]
visited = [0]*(n+1)

dfs([], 0)