# 1시간 5분

# dfs
import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, m = map(int, input().split())
relations = defaultdict(set)
setEnemy = [-1] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    relations[a].add(b)
    relations[b].add(a)

setEnemy = [-1] * (n+1)
def dfs(start):
    dq = deque([start])

    while dq:
        cur = dq.popleft()

        for nxt in relations[cur]:
            if setEnemy[nxt] == -1:
                setEnemy[nxt] = (setEnemy[cur] + 1) % 2
                dq.append(nxt)
            else:
                if setEnemy[cur] % 2 == setEnemy[nxt] % 2:
                    return 0
    return 1

for key in relations.keys():
    if setEnemy[key] == -1:
        setEnemy[key] = 1
        result = dfs(key)
    if not result:
        print(0)
        exit(0)

print(1)