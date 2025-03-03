"""
# 주요 정보
1. 트리
2. 도로는 양방향에 cost = 1
3. 경찰서는 모든 도시 / 도로를 감시할 수 있어야 한다.
    - 경찰서는 양방향으로 연결된 도시까지만 감시할 수 있다.
4. 최소 몇 개의 도시에 경찰서를 세워야 할까?

# 풀이 과정
1. dp 활용
    - 현재 노드에 경찰서를 세울 경우, 자식 노드에는 세우든 / 세우지 않든 상관이 없음
    - 현재 노드에 경찰서를 세우지 않을 경우, 자식 노드에는 경찰서를 세워야 함.
"""

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input())
dict = defaultdict(list)
dp = [[0, 1] for _ in range(n+1)]

visited = [False] * (n+1)

def dfs(start):
    for nxt in dict[start]:
        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt)

            dp[start][0] += dp[nxt][1]
            dp[start][1] += min(dp[nxt])

for _ in range(n-1):
    a, b = map(int, input().split())
    dict[a].append(b)
    dict[b].append(a)

visited[1] = True
dfs(1)
print(min(dp[1]))
