# 방 번호

# 그리디, 브루트포스
# 시간초과
import sys

n = int(input())
cost = list(map(int, sys.stdin.readline().split()))
m = int(input())

result = []
answer = 0
def dfs():
    global m, n, answer, cur
    for i in range(n-1, -1, -1):
        if m - cost[i] >= 0:
            m -= cost[i]
            result.append(str(i))
            dfs()
            m += cost[i]
            result.pop()
    else:
        if len(result) < 1:
            tmp = 0
        else:
            tmp = int("".join(result))
        if answer < tmp:
            answer = tmp

dfs()
        
print(answer)

# 단순 구현
from collections import deque

n = int(input())
lst = list(map(int, input().split()))
m = int(input())
cost = []

for i in range(n):
    cost.append((i, lst[i])) # idx, cost

cost.sort(key = lambda x: x[1])

if cost[0][0] == 0:
    if n == 1 or cost[1][1] > m:
        print(0)
        exit(0)
    else:
        left = m - cost[1][1]
        answer = deque([cost[0]] * (left // cost[0][1]))
        total = cost[0][1] * (left // cost[0][1])
        answer.appendleft(cost[1])
        total += cost[1][1]
else:
    answer = deque([cost[0]] * (m // cost[0][1])) # 만들 수 있는 최대 길이의 배열
    total = cost[0][1] * (m//cost[0][1]) # tmp를 만들기 위해 필요한 총비용

for i in range(len(answer)): # 최대 값부터 변경
    past = answer[i][1]
    for idx in range(answer[i][0]+1, n): # 가능한 최대 값을 찾음
        if total - answer[i][1] + lst[idx] <= m:
            answer[i] = (idx, lst[idx])
            total += (lst[idx] - past)
            past = lst[idx]

result = ""
for case in answer:
    result += str(case[0])
print(result)

# dp⭐️⭐️⭐️⭐️
# 가격에 대한 dp를 생성한다.
# dp[i]는 가격 i일 때 살 수 있는 방의 최대 번호이다.
# 높은 가격이 높은 자리수에 있어야 하므로 n-1 ~ 0으로 반복문을 진행한다.

import sys

n = int(input())
p = list(map(int, input().split()))
m = int(input())
dp = [-float("inf") for _ in range(m+1)]

for i in range(n-1, -1, -1):
    price = p[i]
    for j in range(price, m+1):
        dp[j] = max(dp[j], i, dp[j-price]*10+i)

print(dp)
    