"""
풀이 과정
새로운 사건을 처리할 때 알아야 할 정보
- 두 경찰차의 위치
dp[i][j]
- 첫 번째 경찰자가 i번째 사건 위치에 있는 경우 + 두 번째 경찰차가 j번째 사건 위치에 있는 경우
- next = max(i, j) + 1
- dp[next][j] = min(dp[next][j], dp[i][j] + dist(i, next))
- dp[i][next] = min(dp[i][next], dp[i][j] + dist(j, next))
"""

"""
경로 출력 (dp 역추적 필요)
- 비트 활용
"""

import sys
input = sys.stdin.readline

class DP:
    def __init__(self):
        self.min_dist = sys.maxsize
        self.route = 1

def get_dist(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

n = int(input())
w = int(input())
events = []
for _ in range(w):
    events.append(list(map(int, input().split())))

dp = [[DP() for _ in range(w+1)] for _ in range(w+1)]
FIRST_CAR_START = [1, 1]
SECOND_CAR_START = [n, n]

dp[0][0].min_dist = 0

# 첫 번째 경찰차가 i번째 사건을 담당하고
# 두 번째 경찰차가 j번째 사건을 담당할 때
# 최소 이동 거리 기록
for i in range(w):
    for j in range(w):
        # 다음 사건은 i/j 중 큰 값 + 1
        next = max(i, j) + 1
        if next <= w:
            end = events[next-1]
            start = FIRST_CAR_START if i == 0 else events[i-1]
            new_dist = dp[i][j].min_dist + get_dist(start, end)
            if dp[next][j].min_dist > new_dist:
                dp[next][j].min_dist = new_dist
                dp[next][j].route = dp[i][j].route << 1 | 1
            start = SECOND_CAR_START if j == 0 else events[j-1]
            new_dist = dp[i][j].min_dist + get_dist(start, end)
            if dp[i][next].min_dist > new_dist:
                dp[i][next].min_dist = new_dist
                dp[i][next].route = dp[i][j].route << 1

result_dist = sys.maxsize
result_route = 1
for i in range(w+1):
    if dp[-1][i].min_dist < result_dist:
        result_dist = dp[-1][i].min_dist
        result_route = dp[-1][i].route
    if dp[i][-1].min_dist < result_dist:
        result_dist = dp[i][-1].min_dist
        result_route = dp[i][-1].route

print(result_dist)
for r in bin(result_route)[3:]:
    if r == '1':
        print(1)
    else:
        print(2)