# 다익스트라
import sys
from collections import defaultdict, deque
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra1(start, end): # 전체경로를 저장하는 방식
    cost = [[INF, []] for _ in range(n+1)]
    cost[start] = [0, [start]]
    dq = deque([(start, 0)])

    while dq:
        cur, c = dq.popleft()

        if cost[cur][0] < c: # 이전 cost 값이 더 작을 경우
            continue

        for nxt, nxt_c in road[cur]:
            if cost[cur][0] + nxt_c < cost[nxt][0]: # 더 작은 값으로 비용 업데이트
                cost[nxt][0] = cost[cur][0] + nxt_c
                cost[nxt][1] = cost[cur][1] + [nxt]
                dq.append((nxt, cost[cur][0]+nxt_c))

    print(cost[end][0])
    print(len(cost[end][1]))
    for i in cost[end][1]:
        print(i, end = " ")

def dijkstra2(start, end): # 부모만을 저장하는 방식
    cost = [[INF, -1] for _ in range(n+1)]
    cost[start] = [0, -1]
    dq = deque([(start, 0)])

    while dq:
        cur, c = dq.popleft()

        if cost[cur][0] < c: # 이전 cost 값이 더 작을 경우
            continue

        for nxt, nxt_c in road[cur]:
            if cost[cur][0] + nxt_c < cost[nxt][0]: # 더 작은 값으로 비용 업데이트
                cost[nxt][0] = cost[cur][0] + nxt_c
                cost[nxt][1] = cur
                dq.append((nxt, cost[cur][0]+nxt_c))

    print(cost[end][0])

    path = []
    cur = end
    while cur != -1:
        path.append(str(cur))
        cur = cost[cur][1]
    path.reverse()    
    print(len(path))
    print(" ".join(path))

def dijkstra3(start, end): # 우선순위 큐를 이용한 dijkstra의 정석
    dq = []
    heappush(dq, (0, start))
    cost = [[INF, []] for _ in range(n+1)]
    cost[start] = [0, [start]]

    while dq:
        c, cur = heappop(dq)

        if cost[cur][0] < c: # 이전 cost 값이 더 작을 경우
            continue

        for nxt, nxt_c in road[cur]:
            if cost[cur][0] + nxt_c < cost[nxt][0]: # 더 작은 값으로 비용 업데이트
                cost[nxt][0] = cost[cur][0] + nxt_c
                cost[nxt][1] = cost[cur][1] + [nxt]
                heappush(dq, (cost[cur][0]+nxt_c, nxt))

    print(cost[end][0])
    print(len(cost[end][1]))
    for i in cost[end][1]:
        print(i, end = " ")

n = int(input())
m = int(input())

road = defaultdict(list)
for _ in range(m):
    s, e, c = map(int, input().split())
    road[s].append((e, c))

start, end = map(int, input().split())
dijkstra3(start, end)