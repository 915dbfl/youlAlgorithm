"""
풀이과정
- 새로운 음을 처리할 때 알아야 할 점
    - 두 사람이 바로 직전에 불렀던 음에 대한 정보
- dp[i][j]
    - next = 두 음 중 더 큰 값 (해당 값까지 불렀다는 의미)
    - dp[next][j] = min(dp[next][j], dp[i][j] + abs(sound[next] - sound[i]))
    - dp[i][next] = min(dp[i][next], dp[i][j] + abs(sound[next] - sound[j]))
"""

import sys
input = sys.stdin.readline

n = int(input())
sound = list(map(int, input().split()))

dp = [[sys.maxsize] * (n+1) for _ in range(n+1)]
dp[0][0] = 0
dp[0][1] = 0
dp[1][0] = 0

for i in range(n):
    for j in range(n):
        next = max(i, j) + 1
        if next <= n:
            diff = 0 if i == 0 else abs(sound[next-1] - sound[i-1])
            dp[next][j] = min(dp[next][j], dp[i][j] + diff)
            diff = 0 if j == 0 else abs(sound[next-1] - sound[j-1])
            dp[i][next] = min(dp[i][next], dp[i][j] + diff)

answer = sys.maxsize
for i in range(1, n+1):
    answer = min(answer, dp[i][-1], dp[-1][i])
print(answer)