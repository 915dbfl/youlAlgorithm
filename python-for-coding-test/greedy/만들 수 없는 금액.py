# 기출 문제
# 한 번 더 봐야하는 문제

from itertools import combinations

n = int(input())
nums = list(map(int, input().split()))

lst = set()
for i in range(1, n+1):
    for case in combinations(nums, i):
        lst.add(sum(case))

lst = list(lst)
for i in range(len(lst)-1):
    if lst[i] + 1 != lst[i+1]:
        print(lst[i]+1)
        break

# 해설 풀이
n = int(input())
nums = list(map(int, input().split()))
nums.sort()

target = 1
for num in nums:
    if target < num:
        break
    target += num

print(target)