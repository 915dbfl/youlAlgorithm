# 다익스트라 -> ElogV

import sys
from collections import defaultdict
from heapq import heappop, heappush

input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start, end):
    hq = []
    heappush(hq, (0, start))
    dist = [INF] * (v+1)
    dist[start] = 0

    while hq:
        weight, cur = heappop(hq)

        if weight > dist[cur]:
            continue

        for nxt_weight, nxt_idx in dic[cur]:
            new_dist = weight + nxt_weight
            if new_dist < dist[nxt_idx]:
                dist[nxt_idx] = new_dist
                heappush(hq, (new_dist, nxt_idx))

    return dist[end]
    
v, e, p = map(int, input().split())

dic = defaultdict(list)
for _ in range(e):
    s, e, c = map(int, input().split())
    dic[e].append((c, s))
    dic[s].append((c, e))

if dijkstra(1, p) + dijkstra(p, v) <= dijkstra(1, v):
    print("SAVE HIM")
else:
    print("GOOD BYE")