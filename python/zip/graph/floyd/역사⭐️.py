# 위상정렬 - 오답
# 그래프가 여러 개로 나뉜다면 위상정렬로 문제를 풀이할 수 없음
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
parent = [0] * (n+1)
child = [[] for _ in range(n+1)]

for _ in range(k):
    p, c = map(int, input().split())
    parent[c] += 1
    child[p].append(c)

dq = deque()
order = [-1] * (n+1)
for i in range(1, n+1):
    if parent[i] == 0 and len(child[i]) > 1:
        dq.append(i)
        order[i] = 1

while dq:
    cur = dq.popleft()

    for ch in child[cur]:
        if parent[ch] > 0:
            parent[ch] -= 1
            order[ch] = max(order[ch], order[cur] + 1)
            if (parent[ch] == 0):
                dq.append(ch)

s = int(input())
for _ in range(s):
    i1, i2 = map(int, input().split())
    if order[i1] == -1 or order[i2] == -1: 
        print(0)
        continue

    if order[i1] < order[i2]:
        print(-1)
    elif order[i1] == order[i2]:
        print(0)
    else:
        print(1)

# 플로이드 워샬
import sys
from collections import defaultdict
input = sys.stdin.readline

# O(400 * 400 * 400)
def floyd():
    for i in range(1, n+1):
        dist[i][i] = True

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if not dist[i][j] and (dist[i][k] and dist[k][j]):
                    dist[i][j] = True


n, k = map(int, input().split())
dist = [[False] * (n+1) for _ in range(n+1)]
for _ in range(k):
    i1, i2 = map(int, input().split())
    dist[i1][i2] = True

floyd()

s = int(input())
for _ in range(s):
    i1, i2 = map(int, input().split())
    if dist[i1][i2]:
        print(-1)
    elif dist[i2][i1]:
        print(1)
    else:
        print(0)

# 다익스트라
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n,k = map(int,input().split())
distance = [[401]*(n+1) for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(k):
    x,y = map(int,input().split())
    graph[x].append((y,1))

# ElogV * E = E**2
def dijkstra(start):
    hq = []
    heappush(hq,(0,start))
    distance[start][start] = 0
    while hq:
        dist,now = heappop(hq)

        if distance[start][now] < dist:
            continue

        for i in graph[now]:
            if distance[start][i[0]] > dist+i[1]:
                distance[start][i[0]] = dist+i[1]
                heappush(hq,(dist+i[1],i[0]))

for i in range(1,n+1):
    dijkstra(i)

s = int(input())
for _ in range(s):
    x,y = map(int,input().split())
    if distance[x][y]<401:
        print(-1)
    elif distance[y][x]<401:
        print(1)
    else:
        print(0)