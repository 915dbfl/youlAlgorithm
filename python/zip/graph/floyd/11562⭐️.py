# 다익스트라, 만들어야 하는 최소 길을 구하자!(오답)

# 다익스트라로 해결하면 안되는 이유
# 모든 정점에서 다른 모든 정점으로의 최단 거리를 구해야 한다.
# 다익스트라로 해결할 경우, a -> b일 경우, a -> c -> b가 더 짧을 때 이를 반영하지 못하게 된다.

import sys
from collections import defaultdict
from heapq import heappop, heappush
input = sys.stdin.readline

def bfs(s):
    hq = []
    heappush(hq, (0, s)) # 통행료, 현재 위치

    while hq:
        haveToMake, cur = heappop(hq)

        if cost[s][cur] < haveToMake:
            break

        for c, nxt in road[cur]:
            if cost[s][nxt] > haveToMake + c:
                cost[s][nxt] = haveToMake + c
                heappush(hq, (haveToMake + c, nxt))

n, m = map(int, input().split())
road = defaultdict(list)

for _ in range(m):
    u, v, b = map(int, input().split())
    road[u].append((0, v)) # 해당 도로를 지나는 데 드는 비용(즉, 만들어야 하나 만들지 않아도 되나를 통행료로 생각), 도착지
    if b == 1: # 양방통행
        road[v].append((0, u)) # 만들지 않아도 되는 길, 도착지
    else:
        road[v].append((1, u)) # 만들어야 하는 길, 도착지

k = int(input())
cost = [[n for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    cost[i][i] = 0
    bfs(i)

for _ in range(k):
    s, e = map(int, input().split())
    print(cost[s][e])

# 플로이드 워샬
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

cost = [[n for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1): # 자기 자신으로 가는 길 0으로 초기화
    cost[i][i] = 0
for _ in range(m):
    u, v, b = map(int, input().split())
    cost[u][v] = 0
    if b == 0: # 일방향
        cost[v][u] = 1
    else: # 양방향
        cost[v][u] = 0


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if cost[i][j] > cost[i][k] + cost[k][j]:
                cost[i][j] = cost[i][k] + cost[k][j]

k = int(input())
for _ in range(k):
    s, e = map(int, input().split())
    print(cost[s][e])