# dp

# 이차원 배열을 활용한 풀이
import sys
word1 = sys.stdin.readline().rstrip()
word2 = sys.stdin.readline().rstrip()
h, w = len(word1), len(word2)
dp = [[0] * (w+1) for _ in range(h+1)]

for i in range(1, h+1):
    for j in range(1, w+1):
        if word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])

# 일차원 배열을 이용한 풀이
import sys

import sys
word1 = sys.stdin.readline().rstrip()
word2 = sys.stdin.readline().rstrip()
l1, l2 = len(word1), len(word2)
dp = [0] * l2

for i in range(l1):
    cnt = 0
    for j in range(l2):
        if cnt < dp[j]:
            cnt = dp[j]
        elif word1[i] == word2[j]:
            dp[j] = cnt + 1

print(dp)