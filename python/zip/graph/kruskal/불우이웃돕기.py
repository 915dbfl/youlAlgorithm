"""
- 최소 스패닝 트리 
- 전선 길이 heapq에 저장
- parent 저장
- heapq가 빌 동안 union find 진행
    - a, b가 union이 필요할 경우
    - 사용된 전선에 기록
- 결과 구하기
    - 그래프가 나눠져 있다면 -1
    - 모든 parent가 하나로 연결된다면 전체 전선 - 사용 전선
"""

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def real_dist(alpha):
    if alpha.isdigit(): return 0
    elif alpha.islower(): return ord(alpha) - ord('a') + 1
    else: return ord(alpha) - ord('A') + 27

def find(target):
    if parent[target] != target:
        parent[target] = find(parent[target])
    return parent[target]

def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb

n = int(input())
total = 0
graph = []
for _ in range(n):
    row = list(map(real_dist, list(input().rstrip())))
    total += sum(row)
    graph.append(row)

# 전선 길이 heapq에 저장
hq = []
for i in range(n):
    for j in range(n):
        if i == j: continue
        if graph[i][j] == 0: continue

        heappush(hq, (graph[i][j], i, j))

parent = [i for i in range(n)]
Min = 0
while hq:
    dist, a, b = heappop(hq)
    if find(a) != find(b):
        Min += dist
        union(a, b)

baseP = find(parent[0])
for i in range(1, n):
    if find(i) != baseP:
        print(-1)
        exit(0)

print(total - Min)