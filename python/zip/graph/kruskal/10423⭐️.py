# 다익스트라
import sys
from collections import defaultdict
from heapq import heappop, heappush
input = sys.stdin.readline
Max = 10000

def dijkstra():
    global n
    hq = []
    costs = [Max] * (n+1)
    finish = [False] * (n+1)

    for plant in power_plant:
        costs[plant] = 0
        heappush(hq, (0, plant))

    while hq:
        c, n = heappop(hq)
        if finish[n]:
            continue
        else:
            finish[n] = True
            costs[n] = c
            
            for cost, nxt in cable[n]:
                if not finish[nxt] and cost < costs[nxt]:
                    costs[nxt] = cost
                    heappush(hq, (cost, nxt))

    print(sum(costs[1:]))

n, m, k = map(int, input().split())
power_plant = list(map(int, input().split()))

cable = defaultdict(list)
for _ in range(m):
    u, v, w = map(int, input().split())
    cable[u].append((w, v))
    cable[v].append((w, u))

dijkstra()

# 최소 비용 신장 트리
# 루트 즉, 발전소가 있는 city가 여러 개 이지만
# parent를 0으로 두어 하나의 parent로 부터 출발한 것으로 판단

import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        return find_parent(parent[x])
    return x

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m, k = map(int, input().split())
power = list(map(int, input().split()))

parent = [0] * (n+1)
cable = []

# 부모 초기화
for i in range(1, n+1):
    if i in power: # 발전소라면
        parent[i] = 0 # 0으로 부모 통일⭐️
    else: # 발전소가 아니라면
        parent[i] = i # 자기 자신으로 부모 설정

for _ in range(m):
    u, v, w = map(int, input().split())
    cable.append((w, u, v))

cable.sort()
result = 0

for w, u, v in cable:
    if find_parent(u) != find_parent(v):
        union_parent(u, v)
        result += w

print(result)