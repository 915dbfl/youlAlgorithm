# 다익스트라

import sys
from heapq import heappush, heappop
from collections import defaultdict
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(n):
    hq = []
    heappush(hq, (0, 0)) # dist, cur(현재위치)
    dist = [INF] * n
    dist[0] = 0

    while hq:
        dis, cur = heappop(hq)

        if dist[cur] < dis: continue

        for d, nxt in graph[cur]:
            if dist[nxt] > dis + d:
                # 상대편 넥서스가 아닌데 적에게 노출되는 경우 이동 x
                if exposed[nxt] == 1 and nxt != n-1:
                    continue
    
                dist[nxt] = dis + d
                heappush(hq, (dis+d, nxt))

    print(dist[-1] if dist[-1] != INF else -1)

n, m = map(int, input().split())
exposed = list(map(int, input().split()))

# 분기점을 잇는 길 입력 받기
graph = defaultdict(list)
for _ in range(m):
    a, b, t = map(int, input().split())
    # 연결은 양방향이므로 a, b 양쪽에 해당 연결 저장
    graph[a].append((t, b))
    graph[b].append((t, a))

# dijkstra 실행, 출발점은 0
dijkstra(n)
