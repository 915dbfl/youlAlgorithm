#22.11.17
#n과 m(4)
#class4/실버3
#백트래킹

#중복조합: combination with replacement
from itertools import combinations_with_replacement

n, m = map(int, input().split())
lst = range(1, n+1)

for i in combinations_with_replacement(lst, m):
  print(*i)

#백트래킹
def dfs(cur):
  if len(lst) == m:
    print(*lst)
    return

  else:
    for i in range(cur, n+1):
      lst.append(i)
      dfs(i)
      lst.pop()

n, m = map(int, input().split())
lst = []

dfs(1)