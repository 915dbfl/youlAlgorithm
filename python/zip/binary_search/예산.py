# 1시간

import sys
input = sys.stdin.readline

n = int(input())
budgets = list(map(int, input().split()))
total = int(input())

budgets.sort()
left = 1
right = budgets[-1]

def findIndex(target):
    l = 0
    r = n-1

    while l <= r:
        mid = (l + r) // 2
        if target >= budgets[mid]:
            l = mid + 1
        else:
            r = mid -1

    return r

# 누적합 구하기
prefix = [budgets[0]]
for i in range(1, n):
    prefix.append(prefix[-1] + budgets[i])

# 이분 탐색 구하기
while left <= right:
    mid = (left + right) // 2

    index = findIndex(mid)
    totalCase = 0
    if (index == -1):
        totalCase = mid * n
    else:
        totalCase = prefix[index] + mid * (n - index -1)

    if total >= totalCase:
        left = mid + 1
    else:
        right = mid -1

print(right)

# 다른 풀이

import sys
input = sys.stdin.readline

n = int(input())
costs = list(map(int, input().split()))
total = int(input())

costs.sort()
max = 0
sum = 0

for i in range(n):
    if costs[i] * (n - i) + sum <= total:
        max = costs[i]
        sum += costs[i]
    else:
        max = (total - sum) // (n-i)
        break

print(max)