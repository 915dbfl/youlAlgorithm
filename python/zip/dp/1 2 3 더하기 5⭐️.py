import sys
input = sys.stdin.readline

dp = [[0, 0, 0] for _ in range(100001)]
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, 100001):
    # 1을 붙일 수 있는 경우 카운트
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 1000000009
    # 2를 붙일 수 있는 경우 카운트
    dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % 1000000009
    # 3을 붙일 수 있는 경우 카운트
    dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % 1000000009

t = int(input())
for _ in range(t):
    n = int(input())
    print(sum(dp[n]) % 1000000009)