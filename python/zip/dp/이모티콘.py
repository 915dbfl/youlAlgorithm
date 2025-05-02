# 이모티콘(50분)

"""
풀이과정
1. dp 활용
2. n의 배수를 반복문을 통해 확인 -> 최소 시간 기록

=> 약수를 활용 해야 함
- 6: 1, 2, 3, 6

=> dp를 활용할 수 있을 것 같음
- dp[i]는 i를 만들기 위해 필요한 최소 시간
"""
import sys
input = sys.stdin.readline

s = int(input())

dp = [i for i in range(1001)]
dp[1] = 0

for i in range(2, 501):
    for j in range(i + i, 1001, i):
        time = (j // i) - 1
        dp[j] = min(dp[j], dp[i] + time + 1)
        dp[j-1] = min(dp[j-1], dp[j] + 1)

print(dp[s])

# bfs -> 모든 경우의 수를 확인하는 방법

import sys
from collections import deque
input = sys.stdin.readline

S = int(input())
visited = [[0] * 1001 for _ in range(1001)]

def bfs():
    dq = deque()
    dq.append((1, 0)) # (화면 속 이모티콘 개수, 클립보드 속 이모티콘 개수)

    while dq:
        si, ci = dq.popleft()
        if si == S:
            return visited[si][ci]
    
        arr = [(si, si), (si + ci, ci), (si - 1, ci)]
        for s, c in arr:
            if 0 <= s < 1001 and 0 <= c < 1001:
                if not visited[s][c]:
                    dq.append((s, c))
                    visited[s][c] = visited[si][ci] + 1

print(bfs())