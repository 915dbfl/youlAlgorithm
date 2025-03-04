"""
# 주요 정보
1. 초기 왼손 엄지는 4, 오른손 엄지는 6에 둔다.
2. 움직이는 위치에 따라 가중치가 달라진다.
    - 제자리 1
    - 상하좌우 인접 2
    - 대각선 3
3. 만약 제자리 / 인접하지 않을 경우, 최소 경로로 이동
4. 최종적으로 최소 가중치 합 출력
"""""

# 시간 초과
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

answer = sys.maxsize
dict = defaultdict(list)

# 두 위치 사이 최소 거리 구하기
def cal_min_dis(start, end):
    x_diff = abs(start[0] - end[0])
    y_diff = abs(start[1] - end[1])
    
    # 대각선으로 이동이 필요한 경우
    if x_diff > 0 and y_diff > 0:
        time = min(x_diff, y_diff)
        weight += 3 * time
        x_diff -= time
        y_diff -= time
    # 직선으로 이동이 필요한 경우
    if x_diff > 0 or y_diff > 0:
        time = x_diff if x_diff > 0 else y_diff
        weight += 2 * time
        x_diff = max(0, x_diff - time)
        y_diff = max(0, y_diff - time)
    return weight

def dfs(numbers, index, weight_sum, left, right):
    global answer
    if index == len(numbers):
        answer = min(answer, weight_sum)
        return
    
    if answer <= weight_sum:
        return
    
    num_xy = dict[numbers[index]]
    # 두 손이 겹치지 않는 모든 경우 확인 
    if num_xy == left:
        dfs(numbers, index+1, weight_sum + 1, num_xy, right)
    elif num_xy == right:
        dfs(numbers, index+1, weight_sum + 1, left, num_xy)
    else:
        # 최소 가중치 구하기
        left_min = cal_min_dis(left, num_xy)
        right_min = cal_min_dis(right, num_xy)
        dfs(numbers, index+1, weight_sum + left_min, num_xy, right)
        dfs(numbers, index+1, weight_sum + right_min, left, num_xy)
    
def solution(numbers):
    left = [1, 0]
    right = [1, 2]
    
    # 각 숫자 위치 dictionary에 저장
    for i in range(3):
        for j in range(3):
            dict[str(i*3 + j + 1)] = [i, j]
    dict['0'] = [3, 1]
        
    dfs(numbers, 0, 0, left, right)
    return answer
        
# dp 처리 -> 시간 초과
import sys
from collections import deque
sys.setrecursionlimit(10**6)

def solution(numbers):

    def bfs(idx, L, R, cost):
        dq = deque()
        dq.append((idx, L, R, cost))
        
        while dq:
            ci, cl, cr, cc = dq.popleft()

            if ci == len(numbers): #end
                return

            GOAL = int(numbers[ci])
            L_COST = weight(cl, GOAL)
            R_COST = weight(cr, GOAL)

            #recursive
            if cr != GOAL:
                if cc + L_COST < dp[ci][GOAL][cr]: #left
                    dp[ci][GOAL][cr] = cc + L_COST
                    dq.append((ci+1, GOAL, cr, cc + L_COST))

            if cl != GOAL:
                if cc + R_COST < dp[ci][cl][GOAL]: #right
                    dp[ci][cl][GOAL] = cc + R_COST
                    dq.append((ci+1, cl, GOAL, cc + R_COST))

    def weight(start, end):
        start = pad[start]
        end = pad[end]
        diff = [abs(end[0]-start[0]), abs(end[1]-start[1])]
        common = min(diff)
        other = max(diff)
        return max(common * 3 + ((other - common) * 2), 1)

    answer = 987654321
    pad = {0: (4, 2)}
    INF = 987654321
    L = 4
    R = 6

    for i in range(1, 4):
        for j in range(1, 4):
            pad[j + ((i-1) * 3)] = (i, j)

    dp = [[[INF for i in range(10)] for j in range(10)] for k in range(len(numbers))]

    bfs(0, L, R, 0)

    end = int(numbers[-1])
    for i in range(10):
        answer = min(answer, dp[len(numbers)-1][end][i], dp[len(numbers)-1][i][end])

    return answer