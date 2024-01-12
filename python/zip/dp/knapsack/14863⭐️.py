# # bfs, bruteforce
# import sys
# from collections import deque

# n, k = map(int, input().split())
# walking = []
# cycle = []
# answer = 0

# for _ in range(n):
#     wt, wc, ct, cc = map(int, sys.stdin.readline().split())
#     walking.append((wt, wc))
#     cycle.append((ct, cc))

# def bfs():
#     dq = deque([(1, 0, 0)]) # 현재 구간, 소요된 시간, 모금액
#     global answer

#     while dq:
#         section, time, cost = dq.popleft()

#         if section-1 == n:
#             answer = max(cost, answer)
#             continue

#         if time + walking[section-1][0] <= k: # 다음 구간을 도보로 이동 가능할 경우
#             dq.append((section+1, time + walking[section-1][0], cost + walking[section-1][1]))
        
#         if time + cycle[section-1][0] <= k: # 다음 구간을 자전거로 이동 가능할 경우
#             dq.append((section+1, time + cycle[section-1][0], cost + cycle[section-1][1]))

# bfs()
# print(answer)

# 냅색 문제 응용편
import sys
MAX = sys.maxsize

# go: 현재 idx번째 경로에서 남은 시간이 total일 때 얻을 수 있는 최대 모금액 리턴
def go(idx, total):
    # 시간 예외 처리
    if total < 0:
        return - MAX
    
    # 경산까지 이미 도달한 경우
    if idx == n:
        return 0
    
    # 구해진 값이 있다면 재활용
    if dp[idx][total] != -1:
        return dp[idx][total]
    
    # 점화식
    dp[idx][total] = max(
        (go(idx + 1, total - arr[idx][0]) + arr[idx][1]),
        (go(idx + 1, total - arr[idx][2]) + arr[idx][3])
    )
    return dp[idx][total]

n, k = map(int, sys.stdin.readline().split())
dp = [[-1] * (k+1) for _ in range(n)]
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(go(0, k))