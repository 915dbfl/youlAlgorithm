# 극장 좌석
# dp

import sys

n = int(input())
m = int(input())
fixed = []

for _ in range(m):
    p = int(sys.stdin.readline())
    fixed.append(p)

dp = [1, 1, 2, 3]
for i in range(4, n+1):
    dp.append(dp[-1] + dp[-2])

cur = 0
answer = 1
for f in fixed:
    answer *= dp[f-cur-1]
    cur = f

print(answer * dp[n-cur])