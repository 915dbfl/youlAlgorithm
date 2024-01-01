#22.11.21
#n과 m(9)
#class4/실버2

#순열: permutation
from itertools import permutations

n, m = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()
check = set()

for case in permutations(lst, m):
  if case not in check:
    print(*case)
    check.add(case)

#백트래킹
def dfs():
  if len(answer) == m and tuple(answer) not in check:
    print(*answer)
    check.add(tuple(answer))
  
  for i in range(n):
    if visited[i] == 0:
      visited[i] = 1
      answer.append(lst[i])
      dfs()
      answer.pop()
      visited[i] = 0

n, m = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()
visited = [0]*n
check = set()
answer = []

dfs()

#백트래킹 최적화
def dfs():
  if len(answer) == m:
    print(*answer)
  
  overlap = 0
  for i in range(n):
    if visited[i] == 0 and overlap != lst[i]:
      visited[i] = 1
      answer.append(lst[i])
      overlap = lst[i]
      dfs()
      answer.pop()
      visited[i] = 0

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

visited = [0]*n
answer = []

dfs()