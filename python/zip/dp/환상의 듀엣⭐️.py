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
sounds = list(map(int, input().split()))
dp = [[sys.maxsize] * (n+1) for _ in range(n+1)]

dp[0][0] = 0
dp[1][0] = 0
dp[0][1] = 0

# 상덕이가 i번째 음을 부르고
# 희원이가 j번째 음을 부를 때
# 힘든 정보의 최소값을 dp에 저장
for i in range(n):
    for j in range(n):
        # 두 위치 중 큰 값 + 1이 다음 부를 음
        next = max(i, j) + 1
        # 부를 수 있는 음이라면
        if next <= n:
            hard = 0 if i == 0 else abs(sounds[i-1] - sounds[next-1])
            dp[next][j] = min(dp[next][j], dp[i][j] + hard)
            hard = 0 if j == 0 else abs(sounds[j-1] - sounds[next-1])
            dp[i][next] = min(dp[i][next], dp[i][j] + hard)

answer = sys.maxsize
for i in range(n+1):
    answer = min(answer, dp[-1][i], dp[i][-1])

print(answer)