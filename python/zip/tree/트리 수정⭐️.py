# 문제 접근
# 트리 하나에서 간선 하나를 지웠을 때 -> 트리 두개가 생김
# 두 트리 중 최대 지름 구하기 + 지운 간선 더해주기
# 위의 값이 최대 값일 떄를 구한다.

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input())
graph = defaultdict(list)
edges = []

def bfs(start):
    visited = [-1] * (n+1)
    visited[start] = 0
    dq = deque([(start, 0)])
    max_dist = (start, 0)

    while dq:
        node, dist = dq.popleft()

        # 방문할 경우 표시!
        visited[node] = dist

        for nxt_cost, nxt_node in graph[node]:
            # 방문되지 않은 노드만 방문
            if visited[nxt_node] == -1:
                new_dist = dist + nxt_cost
                dq.append((nxt_node, new_dist))
                if max_dist[1] < new_dist:
                    max_dist = (nxt_node, new_dist)

    return max_dist    

def get_diameter(start):
    # 임의의 노드 start가 트리 지름 경로에 포함된다면
    # start로부터 가장 먼 노드 farthest_node는 지름의 끝점 중 하나이다.
    farthest_node, _ = bfs(start)
    # start가 끝점이 아닐 수 있기에 farthest_node로 다시 한 번 트리의 지름 탐색
    _, dist = bfs(farthest_node)

    return dist

for _ in range(n-1):
    f, t, c = map(int, input().split())
    graph[f].append((c, t))
    graph[t].append((c, f))
    edges.append((f, t, c))

result = -1e9
for f, t, c in edges:
    graph[f].remove((c, t))
    graph[t].remove((c, f))

    d1 = get_diameter(f)
    d2 = get_diameter(t)

    result = max(result, d1 + d2 + c)

    graph[f].append((c, t))
    graph[t].append((c, f))

print(result)