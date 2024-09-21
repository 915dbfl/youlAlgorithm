import sys
from heapq import heappush, heappop
from collections import defaultdict

input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    hq = []
    dist = [INF] * (n+1)
    dist[start] = 0
    heappush(hq, (0, start))

    while hq:
        curC, curN = heappop(hq)

        if dist[curN] < curC:
            continue
    
        for nxtC, nxtN in graph[curN]:
            if curC + nxtC < dist[nxtN]:
                dist[nxtN] = curC + nxtC
                hq.append((curC + nxtC, nxtN))

    return dist

n, e = map(int, input().split())
graph = defaultdict(list)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

v1, v2 = map(int, input().split())

v1_dist = dijkstra(v1)
v2_dist = dijkstra(v2)

answer = min(v1_dist[1] + v1_dist[v2] + v2_dist[n], v2_dist[1] + v2_dist[v1] + v1_dist[n])
print(answer if answer < INF else -1)