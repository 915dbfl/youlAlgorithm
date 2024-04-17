# napsack 알고리즘
# 고려해야 할 점: 쉬기 시작하면 지침지수가 0이 되기 전에는 다시 달릴 수 없다.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# i분에 달릴 수 있는 거리 입력 받기
dist = [-1]
for _ in range(n):
    dist.append(int(input()))

# napsack을 하기 위한 dp 배열
# dp[i][j] = i분일 때 지침지수가 j일 경우 갈 수 있는 최대 거리
dp = [[0] * (m+1) for _ in range(n+1)]

# dp[i][j]가 될 수 있는 경우
    # dp[i-1][j-1] + i분을 달릴 경우
for i in range(1, n+1):
    for j in range(m+1):
        # 지침지수는 시간과 비례하기 때문에
        # 시간을 넘는 지침지수는 될 수가 없다.
        if i < j: continue
        if j == 0:
            dp[i][j] = max(dp[i-1][j], dp[i][j])
        else:
            dp[i][j] = dp[i-1][j-1] + dist[i]
            # 지침지수 0일때 값 업데이트
            if i+j <= n:
                dp[i+j][0] = max(dp[i+j][0], dp[i][j])

print(dp[-1][0])