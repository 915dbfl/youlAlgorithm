import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline

def connecting():
    global answer
    hq = []

    for p in plants:
        visited[p] = 1
        for cable in cables[p]:
            heappush(hq, cable)

    while hq:
        cost, next = hq[0]
        heappop(hq)
        
        if visited[next] == 0:
            for cable in cables[next]:
                if not visited[cable[1]]:
                    heappush(hq, cable)
        
            answer += cost
            visited[next] = 1
    
    print(answer)

n, m, k = map(int, input().split())
plants = list(map(int, input().split()))

cables = defaultdict(list)
for _ in range(m):
    u, v, w = map(int, input().split())
    cables[u].append((w, v))
    cables[v].append((w, u))

visited = [0 for _ in range(n+1)]
answer = 0
connecting()

# 크루스칼 알고리즘
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def find_parent(target):
    if parent[target] != target:
       parent[target] = find_parent(parent[target])
    
    return parent[target]
    
def union(a, b):
    parentA = find_parent(a)
    parentB = find_parent(b)

    if parentA > parentB:
        parent[parentA] = parentB
    else:
        parent[parentB] = parentA

n, m, k = map(int, input().split())
parent = [i for i in range(n+1)]

plants = list(map(int, input().split()))
for p in plants:
    parent[p] = 0

cable = []
for _ in range(m):
    u, v, c = map(int, input().split())
    heappush(cable, (c, u, v))

answer = 0
while cable:
    cost, city1, city2 = cable[0]
    heappop(cable)

    if find_parent(city1) != find_parent(city2):
        union(city1, city2)
        answer += cost
print(answer)