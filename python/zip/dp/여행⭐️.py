# m개 이하의 도시를 지나는 여행 계획
# 1번 - n번 여행

# 다익스트라: 오답
    # 생각한 원인
    # 단순 경로의 가중치만을 두고 판단하는 것이 아니라
    # 가중치가 작아도 m개 이하 도시에 포함된다면 해당 도로를 포함해야 한다.

# dp 풀이
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
dp = [[0] * (m+1) for _ in range(n+1)]

for _ in range(k):
    s, e, v = map(int, input().split())
    if s > e: continue
    graph[s][e] = max(graph[s][e], v)

for i in range(2, n+1):
    dp[i][2] = graph[1][i]

for i in range(2, n+1):
    for j in range(3, m+1):
        for l in range(1, i):
            if graph[l][i] and dp[l][j-1]:
                dp[i][j] = max(dp[i][j], dp[l][j-1] + graph[l][i])

print(max(dp[n]))