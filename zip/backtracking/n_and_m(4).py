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

#23.06.29
#n과 m(4)
#backtracking

import sys
n, m = map(int, sys.stdin.readline().split())
nums = [i for i in range(1, n+1)]

def dfs(cur, lst):
    global m, n
    if len(lst) == m:
        print(*lst)
    elif cur <= (n-1):
        for i in range(cur, n):
            lst.append(nums[i])
            dfs(i, lst)
            lst.pop()

dfs(0, [])

# 다른 풀이
n, m = map(int, input().split())
s = []

def dfs(start):
    if len(s) == m:
        print(*s)
    else:
        for i in range(start, n+1):
            s.append(i)
            dfs(i)
            s.pop()

dfs(1)