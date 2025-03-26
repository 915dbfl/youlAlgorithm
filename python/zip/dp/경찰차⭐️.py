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
- evnet_cnt size 배열 활용
"""

import sys
input = sys.stdin.readline

class Dist:
    def __init__(self):
        self.minDist = sys.maxsize
        self.route = 1

def dist(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

n = int(input())
event_cnt = int(input())
events = []
for _ in range(event_cnt):
    events.append(list(map(int, input().split())))

dp = [[Dist() for _ in range(event_cnt + 1)] for _ in range(event_cnt + 1)]
dp[0][0].minDist = 0
FIRST_CAR_XY = [1, 1]
SECOND_CAR_XY = [n, n]

# 첫 번째 경찰차가 i번째 사건을 처리하는 경우
# 두 번째 경찰차가 j번째 사건을 처리하는 경우
for i in range(event_cnt):
    for j in range(event_cnt):
        next = max(i, j) + 1
        if next <= event_cnt:
            # 첫 번째 경찰차가 이동하는 경우
            before = FIRST_CAR_XY if i == 0 else events[i-1]
            newDist = dp[i][j].minDist + dist(before, events[next-1])
            if dp[next][j].minDist > newDist:
                dp[next][j].minDist = newDist
                dp[next][j].route = (dp[i][j].route << 1) | 1
            
            # 두 번째 경찰차가 이동하는 경우
            before = SECOND_CAR_XY if j == 0 else events[j-1]
            newDist = dp[i][j].minDist + dist(before, events[next-1])
            if dp[i][next].minDist > newDist:
                dp[i][next].minDist = newDist
                dp[i][next].route = dp[i][j].route << 1

answer = sys.maxsize 
final_route = []
for i in range(event_cnt):
    if answer > dp[i][-1].minDist:
        final_route = dp[i][-1].route
        answer = dp[i][-1].minDist
    if answer > dp[-1][i].minDist:
        final_route = dp[-1][i].route
        answer = dp[-1][i].minDist

print(answer)
for r in bin(final_route)[3:]:
    if r == '1':
        print(1)
    else:
        print(2)