# 징검다리 건너기

# dp로 각 돌까지의 최소 에너지를 저장한다.
# 큰 점프를 하는 경우와 안하는 경우로 dp의 값이 달라지므로
# 두 가지 경우로 나눠 재귀를 돌린다.
import sys
n = int(input())
stone = []

for _ in range(n-1):
    stone.append(list(map(int, sys.stdin.readline().split())))
k = int(input())

dp = [sys.maxsize]*n
dp[0] = 0
def dfs(cur, isJump):
    global answer
    if cur >= n:
        return

    if 0<=cur-1:
        dp[cur] = min(dp[cur-1] + stone[cur-1][0], dp[cur])
    if 0<=cur-2:
        dp[cur] = min(dp[cur-2] + stone[cur-2][1], dp[cur])
    dfs(cur+1, isJump)
    if not isJump and 0 <=cur-3:
        dp[cur] = min(dp[cur-3] + k, dp[cur])
        dfs(cur+1, True)

dfs(0, False)
print(dp[-1])