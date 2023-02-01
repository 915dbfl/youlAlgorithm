#23.02.01
#서강그라운드
#골드4

import sys
from collections import defaultdict, deque

def bfs(start):
    q = deque([(start, 0)])
    visited = [0] * n
    visited[start] = 1
    
    item = 0

    while q:
        cur, l = q.popleft()

        for next, cost in path[cur]:
            if visited[next] == 0:
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