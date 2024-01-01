#23.02.01
#서강그라운드
#골드4

#bfs
#각 지역까지의 최단거리를 파악해야 하지만
#간선의 값이 다른 경우 bfs의 경우 최단경로 순서로 방문하지 않을 수 있다.

# 거리제한 15
#1 -> 2: 10
#1 -> 3: 3
#3 -> 2: 3
#2 -> 4: 6
#1->3->2->4는 12이므로 아이템을 얻을 수 있어야 한다.
#bfs의 경우 1->2->4의 경우 16으로 4를 방문할 수 없다고 판단

#따라서 방문한 노드를 재방문할 수 있게 해야 최단거리를 알 수 있다.
import sys
from collections import defaultdict, deque

def bfs(start): #o(n^2)
    q = deque([(start, 0)])
    visited = [0] * n
    visited[start] = 1
    
    item = 0

    while q:
        cur, l = q.popleft()

        for next, cost in path[cur]:
            if cost + l <= m:
                visited[next] = 1
                q.append((next, cost+l))
    
    for i in range(n):
        if visited[i] == 1:
            item += items[i]

    return item

n, m, r = map(int, sys.stdin.readline().split())
items = list(map(int, sys.stdin.readline().split()))
path = defaultdict(list)

for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    path[a-1].append((b-1, l))
    path[b-1].append((a-1, l))

answer = 0
for i in range(n):
    answer = max(answer, bfs(i))

print(answer)

#플로이드워샬
import sys

n, m, r = map(int, sys.stdin.readline().split())
items = list(map(int, sys.stdin.readline().split()))
path = [[16]*n for _ in range(n)]

for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    path[a-1][b-1] = l
    path[b-1][a-1] = l

for k in range(n): #o(n^3)
    for i in range(n):
        for j in range(n):
            if i == j:
                path[i][j] = 0
                path[j][i] = 0
            elif path[i][j] > path[i][k] + path[k][j]:
                path[i][j] = path[i][k] + path[k][j]

answer = 0
for i in range(n):
    tmp = 0
    for j in range(n):
        if path[i][j] <= m:
            tmp += items[j]
        
    answer = max(answer, tmp)

print(answer)

#다익스트라
#v: 정점의 수, e: 간선의 수
#heap 사용 안할 경우: o(v^2)
#heap 사용 경우: o(eloge)
import sys
from collections import defaultdict
from heapq import heappop, heappush

def dijkstra(start):
    heap = []
    heappush(heap, (0, start))

    costs = [16]*n
    costs[start] = 0

    while heap:
        cost, cur = heappop(heap)

        if cost > costs[cur]:
            continue

        for c, next in path[cur]:
            if cost+c < costs[next]:
                costs[next] = cost+c
                heappush(heap, (cost+c, next))

    return costs


n, m, r = map(int, sys.stdin.readline().split())
items = list(map(int, sys.stdin.readline().split()))
path = defaultdict(list)

for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    path[a-1].append((l, b-1))
    path[b-1].append((l, a-1))

answer = 0
for i in range(n):
    tmp = 0
    for i, v in enumerate(dijkstra(i)):
        if v <= m:
            tmp += items[i]

    answer = max(answer, tmp)

print(answer)