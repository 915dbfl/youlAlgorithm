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
n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
nums = []

def dfs():
   if len(nums) == m:
      print(*nums)
   else:
      for n in lst:
         if n not in nums:
            nums.append(n)
            dfs()
            nums.pop()

dfs()