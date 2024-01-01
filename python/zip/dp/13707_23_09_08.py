# 합분해2

# 2차원 dp
# dp[i][j]: i개를 더하고 j가 되는 경우의 수
# 주의: 메모리 초과
    # 512mb -> 10**6 * 512
    # 10**6 * 5 * 5 * 4byte 
n, k = map(int, input().split())
dp = [[0]*(n+1) for _ in range(k+1)]

for i in range(k+1):
    dp[i][0] = 1

for i in range(1, k+1):
    for j in range(1, n+1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000

print(dp[-1][-1])