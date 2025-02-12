"""
단순히 중복되는 아이템을 추가할 경우 생기는 문제점
- k = 3인 물건 X가 있을 경우, 각각 추가한 아이템을 A, B, C라고 하자.
- 이때 A,B / B,C / A,C를 가져가는 경우에는 아무런 차이가 존재하지 않는다.
- 즉, 2^K 만큼 불필요한 반복이 생기는 것이다.
"""

"""
다중 배낭 문제
핵심 아이디어
- 모든 자연수는 2의 거듭제곱 수로 나타낼 수 있다. 
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
items = []

for _ in range(n):
    w, c, k = map(int, input().split())

    i = 1
    while k > 0:
        m = min(i, k)
        items.append((w * m, c * m))
        k -= i
        i *= 2

dp = [0] * (m+1)
for w, c in items:
    for i in range(m, w-1, -1):
        dp[i] = max(dp[i], dp[i-w] + c)

print(dp[-1])