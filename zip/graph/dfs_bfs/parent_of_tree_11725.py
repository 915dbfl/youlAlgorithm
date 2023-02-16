#23.02.16
#트리의 부모 찾기
#실버2
#알고리즘 스터디: bfs

import sys
from collections import defaultdict, deque

def bfs():
    q = deque([1])

    while q:
        cur = q.popleft()

        for next in dic[cur]:
            if parent[next] == 0:
                parent[next] = cur
                q.append(next)

n = int(sys.stdin.readline())
dic = defaultdict(list)
parent = [0] * (n+1)
parent[1] = -1

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    dic[a].append(b)
    dic[b].append(a)

bfs()
for i in range(2, n+1):
    print(parent[i])