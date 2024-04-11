import sys
from collections import defaultdict
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

# 시간복잡도 O(dn)
def dijkstra(start, n):
    que = []
    dist = [INF] * n
    # 시작위치 dist 초기화
    dist[start] = 0
    heappush(que, (0, start))

    while que:
        c, cur = heappop(que)

        if dist[cur] < c: continue

        for cost, nxt in graph[cur]:
            if dist[nxt] > c + cost:
                dist[nxt] = c + cost
                heappush(que, (c+cost, nxt))

    return dist

n, m, x, y = map(int, input().split())
graph = defaultdict(list)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

distList = dijkstra(y, n)
distList.sort()

# 가장 먼 이웃을 왕복하는 거리가 x보다 멀 때
if distList[-1] * 2 > x:
    print("-1")
else:
    day = 0
    sum = 0
    idx = 1

    # 가까운 집부터 방문
    while(idx < n):
        # 방문할 수 있다면
        if sum + (distList[idx]) * 2 <= x:
            sum += distList[idx] * 2
            idx += 1
        else:
            day += 1
            sum = 0
    
    # 남은 거리를 가기 위해 day + 1
    if sum > 0:
        day += 1

    print(day)