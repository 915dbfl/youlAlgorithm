# 위상 정렬
# 그래프 상에서 선후 관계가 있을 경우, 선후 관계를 지키는 전체 순서 계산 가능
# O(V+E), 차례대로 모든 노드를 확인하면서 노드에서 출발하는 간선 제거

from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# topology-sort
def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    for i in result:
        print(i, end = " ")

topology_sort()