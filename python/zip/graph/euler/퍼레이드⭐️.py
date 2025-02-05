# 오일러 경로 / 회로 + 유니온 파인드
# 경로를 구하지 않아도 되므로 오일로 경로 / 회로 만족 조건을 확인하자!

import sys
from collections import defaultdict
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = list(map(int, input().rstrip().split()))
graph = defaultdict(list)
parent = [i for i in range(v + 1)]

for _ in range(e):
    a, b = list(map(int, input().rstrip().split()))
    if find(a) != find(b): union(a, b)
    graph[a].append(b)
    graph[b].append(a)

p = find(parent[1])
# 모두 연결되지 않은 경우 제외
# parent에 기록된 parent는 실제 parent가 아님의 유의!⭐️
if not all(find(node) == p for node in parent[1:]):
    print("NO")
    exit()

edge = []
for key, value in graph.items():
    if len(value) % 2 == 1:
        edge.append(key)

if (len(edge) in [0, 2]):
    print("YES")
else:
    print("NO")