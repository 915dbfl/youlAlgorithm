# 동전
# dp

import sys
t = int(input())

for _ in range(t):
    n = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    target = int(sys.stdin.readline())
    dp = [0] * (target+1)
    dp[0] = 1

    for c in coins:
        for i in range(target+1):
            if i-c >= 0:
                dp[i] += dp[i-c]
    # 잘못된 풀이
    # dp[t]의 경우 이미 모든 경우의 수가 다 들어갔기 때문에 c를 마이너스 하며
    # 돌 경우 중복이 생기게 된다.
    # for t in range(target+1):
    #     for c in coins:
    #         if t-c >= 0:
    #             dp[t] += dp[t-c]

    print(dp[-1])