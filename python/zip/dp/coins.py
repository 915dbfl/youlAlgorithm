# dp 활용(25분)

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    dp = [0] * (m+1)

    for i in range(n):
        for j in range(coins[i], m+1):
            cur_coin = coins[i]
            if j >= cur_coin:
                dp[j] += dp[j-cur_coin]
            if j == cur_coin:
                dp[j] += 1

    print(dp[-1])