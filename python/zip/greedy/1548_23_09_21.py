# 부분 삼각 수열

import sys
from itertools import combinations

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort()
result = 0
if n < 3:
    print(n)
    exit(0)

for case in combinations(nums, 2):
    Max = max(case)
    total = sum(case)

    s, e = -1, -1
    for i in range(n):
        if s == -1 and nums[i] == Max:
            s = i
            continue 

        if total <= nums[i]:
            e = i -1
            break
    else:
        e = n-1

    if e != -1:
        if case[0] == case[1]:
            if result < (e - s + 1):
                result = e - s + 1
        else:
            if result < (e - s + 2):
                result = e - s + 2

print(result)

# 다른 풀이: 그리디
# 결국 '최소 + 두 번째 최소 > 최대'만 비교하면 되는 것
n = int(input())

nums = list(map(int, input().split()))
nums.sort()

answer = 1
for i in range(n-1):
    for j in range(n-1, -1, -1):
        if j < i + 1:
            continue
        if nums[i] + nums[i+1] > nums[z]:
            answer = max(j-i+1, answer)

print(answer)