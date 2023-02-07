# #23.02.07
# #파티
# #골드3

#플로이드 워셜 - 시간초과
import sys
n, m, x = map(int, sys.stdin.readline().split())
graph = [[100]*n for _ in range(n)]

for _ in range(m):
    s, e, t = map(int, sys.stdin.readline().split())
    graph[s-1][e-1] = t

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0

            elif graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

time = [0]*n
for i in range(n):
    time[i] = graph[i][x-1] + graph[x-1][i]

print(max(time))

#다익스트라 - 오답
import sys
from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(start):
    heap = [(0, start)]

    while heap:
        time, cur = heappop(heap)

        if graph[start][cur] < time:
            continue

        for tmp, next in dic[cur]:
            if graph[start][next] > time + tmp:
                graph[start][next] = time+tmp
                heappush(heap, (time+tmp, next))

n, m, x = map(int, sys.stdin.readline().split())
dic = defaultdict(list)
graph = [[100]*n for _ in range(n)]

for _ in range(m):
    s, e, t = map(int, sys.stdin.readline().split())
    dic[s-1].append((t, e-1))

for i in range(n):
    dijkstra(i)

time = [0]*n
for i in range(n):
    time[i] = graph[i][x-1] + graph[x-1][i]

print(max(time))