# #22.11.18
# #n과 m(5)
# #class4/실버3
#순열/백트래킹

# # permutations 사용하기
from itertools import permutations

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

for case in permutations(lst, m):
  print(*case)

#백트래킹
import sys
sys.setrecursionlimit(10**4)

def dfs():
  if len(lst) == m:
    print(*lst)
    return
  else:
    for num in nums:
      if num not in lst:
        lst.append(num)
        dfs()
        lst.pop()

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

lst = []

dfs()