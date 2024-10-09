# dp

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(n, 0, -1):
    for j in range(1, n+1):
        realRow = abs(n - i) + 1
        if nums[i-1] == nums[j-1]:
            dp[realRow][j] = dp[realRow-1][j-1] + 1
        else:
            dp[realRow][j] = max(dp[realRow-1][j], dp[realRow][j-1])

print(n - dp[-1][-1])