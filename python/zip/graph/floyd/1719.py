# 다익스트라, union-find 결합 문제

import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline

def find_parent(target):
    if parent[target] == "-": # 부모가 없는 경우
        return parent[target]
    
    if target != parent[target]:
        parent[target] = find_parent(parent[target])
    return parent[target]

#cur 부모로 nxt 부모 업데이트
def union(cur, nxt):
    pCur = find_parent(cur)
    pNxt = find_parent(nxt)

    # 둘 중 하나라도 부모가 없을 경우
    if pCur == "-" or pNxt == "-":
        if pCur == "-":
            parent[cur] = pNxt
        elif pNxt == "-":
            parent[nxt] = pCur
        return
    else:
        # cur 부모로 nxt 부모 업데이트
        parent[nxt] = pCur

def dijkstra(start):
    hq = []
    
    for c, nxt in road[start]:
        parent[nxt] = nxt
        visited[nxt] = c
        heappush(hq, (c, nxt))

    while hq:
        cost, cur = heappop(hq)

        if visited[cur] < cost:
            continue

        for c, nxt in road[cur]:
            if cost + c < visited[nxt]:
                union(cur, nxt)
                visited[nxt] = cost+c
                heappush(hq, (cost+c, nxt))

n, m = map(int, input().split())
road = defaultdict(list)

for _ in range(m):
    u, v, c = map(int, input().split())
    road[u].append((c, v))
    road[v].append((c, u))

for i in range(1, n+1):
    visited = [n*1000 for _ in range(n+1)]
    visited[i] = 0
    parent = ["-" for _ in range(n+1)]

    dijkstra(i)
    print(" ".join(map(str, parent[1:])))

# 플로이드 워샬 알고리즘
import sys
input = sys.stdin.readline

INF = 10001

def floyd():
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                # 자기 자신으로 가는 길 우회
                if i == j:
                    continue

                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    # entrance값 업데이트
                    entrance[i][j] = entrance[i][k]

n, m = map(int, input().split())
dist = [[INF for _ in range(n+1)] for _ in range(n+1)]
entrance = [["-" for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    u, v, c = map(int, input().split())
    dist[u][v] = dist[v][u] = c
    entrance[u][v] = str(v)
    entrance[v][u] = str(u)

floyd()
for i in range(1, n+1):
    print(*entrance[i][1:], sep = " ")