#22.11.18
#n과 m(8)
#class4/실버3

#중복조합: combination_with_replacement
from itertools import combinations_with_replacement

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

for case in combinations_with_replacement(lst, m):
  print(*case)


# 백트래킹
def dfs(cur):
  if len(lst) == m:
    print(*lst)
  else:
    for i in range(cur, n):
      lst.append(nums[i])
      dfs(i)
      lst.pop()

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

lst = []

dfs(0)