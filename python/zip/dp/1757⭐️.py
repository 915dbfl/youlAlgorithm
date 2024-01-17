# top-down-dp
# 시간 초과 간당간당~~
import sys
sys.setrecursionlimit(10**4)
MIN = -sys.maxsize

# 지침 지수가 m이고 n분일 때 달릴 수 있는 최대 거리
def sol(cur, amount):
    if cur == n:
        if (amount == 0): return 0
        return MIN
    
    if (dp[cur][amount] != MIN): return dp[cur][amount]

    # 뛰지 않는 경우
    if amount > 0: # 지침이 0이 될때까지 뛰지 못함
        if cur + amount <= n:
            dp[cur][amount] = max(dp[cur][amount], sol(cur + amount, 0))
    else: # 뛸 수 있지만 뛰지 않는 경우
        dp[cur][amount] = max(dp[cur][amount], sol(cur+1, 0))

    # 뛰는 경우
    if amount + 1 <= m:
        dp[cur][amount] = max(dp[cur][amount], sol(cur+1, amount+1) + d[cur])

    return dp[cur][amount]

n, m = map(int, input().split())
d = []

for _ in range(n):
    d.append(int(sys.stdin.readline()))

dp = [[MIN] * (m+1) for _ in range(n)]
print(sol(0, 0))

# 일차원 배열 dp 활용
n, m = map(int, input().split())
dist = [0] + [int(input()) for _ in range(n)]
for i in range(1, n+1):
    dist[i] += dist[i-1]

dp = [0] * (n+1)

for i in range(n):
    for j in range(1, m+1):
        # j만큼 달리면 j만큼 쉬어야 하기 때문에 j를 두 번 더한다.
        # 왜 이걸 생각하지 못했지..
        if i + j + j <= n:
            dp[i+j+j] = max(dp[i+j+j], dp[i] + dist[i+j] - dist[i])
    dp[i+1] = max(dp[i+1], dp[i])
print(dp[-1])