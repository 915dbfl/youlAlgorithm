# 30분

import sys
from collections import defaultdict
input = sys.stdin.readline

n, m, a, b, c = map(int, input().split())
alley = defaultdict(list)

for _ in range(m):
    n1, n2, nc = map(int, input().split())
    alley[n1].append((n2, nc))
    alley[n2].append((n1, nc))

visited = [False] * (n+1)
answer = 10000

def dfs(cur, cost, minMax):
    global answer
    if cost > c: return

    if cur == b:
        answer = min(answer, minMax)
        return
    
    for nxt, ncost in alley[cur]:
        # 한 번 방문한 경우 제외
        if visited[nxt]: continue
        # 금액이 모자를 경우 제외
        totalCost = cost + ncost
        if totalCost > c: continue
        # 이미 구해진 요금의 최댓값의 최솟값을 초과하는 경우
        nMinMax = max(minMax, ncost)
        if nMinMax > answer: continue

        visited[nxt] = True
        dfs(nxt, totalCost, nMinMax)
        visited[nxt] = False

visited[a] = True
dfs(a, 0, 1)
if answer == 10000:
    print(-1)
else:
    print(answer)

# 다익스트라 풀이

import sys
from collections import defaultdict
from heapq import heappop, heappush
input = sys.stdin.readline

n, m, a, b, c = map(int, input().split())
alley = defaultdict(list)

for _ in range(m):
    n1, n2, nc = map(int, input().split())
    alley[n1].append((nc, n2))
    alley[n2].append((nc, n1))

hp = [(0, 0, a)] # 요금 최댓값의 최솟값, total 요금, 현재 위치
minMaxList = [10000] * (n+1)
minMaxList[a] = 0

while hp:
    minMax, totalCost, curNode = heappop(hp)

    # 최종 목적지에 도착했다면 결과값 출력!
    if curNode == b:
        print(minMax)
        exit(0)

    for ncost, nxt in alley[curNode]:
        nTotalCost = totalCost + ncost
        if nTotalCost > c: continue

        nMinMax = max(minMax, ncost)
        if minMaxList[nxt] <= nMinMax: continue

        minMaxList[nxt] = nMinMax
        heappush(hp, (nMinMax, nTotalCost, nxt))

print(-1)