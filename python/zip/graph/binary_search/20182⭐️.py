# 단순 다익스트라
# 부분 정답인 이유
    # 전체 cost는 증가하지만 더 낮은 max_cost를 고려하지 않았기 때문!
import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline

def dijkstra(start, end, budget):
    visited = [(n-1) * 20 for _ in range(n+1)]
    visited[start] = 0
    hq = []
    hq.append((0, start, 0)) # cost, cur, max_cost

    answer = sys.maxsize
    while hq:
        cost, cur, maxC = heappop(hq)

        if (cur != end and visited[cur] < cost) or cost > budget or answer < maxC:
            continue

        if cur == end:
            answer = min(maxC, answer)
            continue

        for c, nxt in road[cur]:
            if nxt == end or (visited[cur] + c < visited[nxt]):
                visited[nxt] = visited[cur] + c
                maxC = max(c, maxC)

                heappush(hq, (visited[cur]+ c, nxt, maxC))

    print(answer if answer != sys.maxsize else -1)

n, m, start, end, budget = map(int, input().split())
road = defaultdict(list)

for _ in range(m):
    u, v, c = map(int, input().split())
    road[u].append((c, v))
    road[v].append((c, u))

if budget < n-1:
    print(-1)
else:
    dijkstra(start, end, budget)

# 다익스트라 + 이진탐색

import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline

def dijkstra(start, end, budget, maxCost):
    visited = [(n-1) * 20 for _ in range(n+1)]
    visited[start] = 0
    hq = []
    hq.append((0, start))
    while hq:
        cost, cur = heappop(hq)

        if cost > visited[cur]:
            continue

        if cur == end:
            if cost <= budget:
                return True

        for c, nxt in road[cur]:
            if c <= maxCost and (cost + c < visited[nxt]):
                visited[nxt] = cost + c
                heappush(hq, (cost + c, nxt))

    return False

n, m, start, end, budget = map(int, input().split())
road = defaultdict(list)

for _ in range(m):
    u, v, c = map(int, input().split())
    road[u].append((c, v))
    road[v].append((c, u))

left = -1
right = 21

while (left <= right):
    mid = (left + right)//2
    # mid를 최대 수치심으로 갈 수 있는가?
    if (dijkstra(start, end, budget, mid)):
        right = mid-1
    else:
        left = mid+1

print(right+1 if right != 21 else -1)
