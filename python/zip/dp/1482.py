import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(2)
else:
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = 1
    dp[0][1] = 3
    dp[1][0] = 2
    dp[1][1] = 7

    for i in range(2, n):
        dp[0][i] = (dp[0][i-1] + dp[1][i-1]) % 1000000007
        dp[1][i] = (dp[0][i] + dp[0][i-1] + dp[1][i-1] + dp[1][i-2]) % 1000000007

    print(dp[-1][-1])
