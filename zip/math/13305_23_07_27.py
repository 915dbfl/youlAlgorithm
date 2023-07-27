#주유소
#단순 구현

# dp: 부분 성공
import sys

n = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))
dp_cost = [sys.maxsize] * n
dp_cost[-1] = 0
dp_road = [0] * n

for i in range(n-2, -1, -1):
    dp_road[i] = roads[i] + dp_road[i+1]
    for j in range(n-1, -1, -1):
        dp_cost[i] = min(dp_cost[i], dp_cost[j] + costs[i] * (dp_road[i] - dp_road[j]))

print(dp_cost[0])

# 다른 풀이
#dp를 안해도 그 시점 가장 값싼 주유소를 선택해 기름을 채우면 된다.
import sys
input = sys.stdin.readline

n = int(input())

roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

#1 -> 2 값 계산
min_price = roads[0] * costs[0]
min_cost = costs[0]

for i in range(1, n-1):
    if costs[i] < min_cost:
        min_cost = costs[i]
    
    min_price += min_cost * roads[i]
print(min_price)