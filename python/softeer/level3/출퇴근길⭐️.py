# s -> x, x -> s, t -> x, x -> t
# 네 가지 경로로 나눠 확인해 시간 초과 방지!

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def bfs(start, graph, v):
    dq = deque([start])
    v[start] = 1

    while dq:
        cur = dq.popleft()

        for nxt in graph[cur]:
            if not v[nxt]:
                v[nxt] = 1
                dq.append(nxt)
    
n, m = map(int, input().split())
graph = defaultdict(list)
graph_v = defaultdict(list)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph_v[y].append(x) # x -> t/s 경로를 확인하기 위해 사용

s, t = map(int, input().split())

# s -> x 확인
fromS = [0] * (n+1)
fromS[t] = 1
bfs(s, graph, fromS)

# x -> s 확인
toS = [0] * (n+1)
toS[t] = 1
bfs(s, graph_v, toS)

# t -> x 확인
fromT = [0] * (n+1)
fromT[s] = 1
bfs(t, graph, fromT)

# x -> t 확인
toT = [0] * (n+1)
toT[s] = 1
bfs(t, graph_v, toT)

answer = 0
for i in range(1, n+1):
    if i not in (s, t):
        if fromS[i] and fromT[i] and toS[i] and toT[i]:
            answer += 1
print(answer)