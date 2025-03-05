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
"""
# dfs로 하면 시간 초과 발생하는 이유
- dfs를 진행할 경우
    - 왼손으로 쭉 이동하는 경우 파악 -> 오른손으로 이동하는 경우 파악
    - 최적의 dp가 설정되지 않아 가지치기가 제대로 되지 않는다.
    -> bfs를 통해 왼손 / 오른손 번갈아 움직이면서 최적의 dp를 빠르게 설정할 수 있다.
"""
from collections import defaultdict, deque
import sys

def cal_weight(xy1, xy2):
    x1, y1 = xy1
    x2, y2 = xy2
    diff1 = abs(x2 - x1)
    diff2 = abs(y2 - y1)
    
    cross = min(diff1, diff2)
    straight = max(diff1, diff2) - cross
    
    return max(1, cross*3 + straight*2)

def solution(numbers):
    # 숫자마다 xy 위치 구하기
    xy_board = defaultdict(list)
    xy_board[0] = [3, 1]
    for i in range(3):
        for j in range(3):
            xy_board[3 * i + j + 1] = [i, j]
    
    # dp 초기화
    dp = defaultdict(lambda: sys.maxsize)
    dp[(4, 6, 0)] = 0
    n = len(numbers)
    
    # bfs 진행
    dq = deque([(4, 6, 0)])
    while dq:
        left, right, idx = dq.popleft()
        if idx == n:
            continue
            
        nxt_num = int(numbers[idx])
        lxy = xy_board[left]
        rxy = xy_board[right]
        nxy = xy_board[nxt_num]        
        
        # 왼손 이동이 가능한 경우
        if nxt_num != right:
            new_cost = dp[(left, right, idx)] + cal_weight(lxy, nxy)
            if new_cost < dp[(nxt_num, right, idx+1)]:
                dp[(nxt_num, right, idx+1)] = new_cost
                dq.append((nxt_num, right, idx+1))
                
        # 오른쪽 이동이 가능한 경우
        if nxt_num != left:
            new_cost = dp[(left, right, idx)] + cal_weight(rxy, nxy)
            if new_cost < dp[(left, nxt_num, idx+1)]:
                dp[(left, nxt_num, idx+1)] = new_cost
                dq.append((left, nxt_num, idx+1))
                
    last_num = int(numbers[-1])
    answer = sys.maxsize
    for i in range(10):
        answer = min(answer, dp[(last_num, i, n)], dp[(i, last_num, n)])
        
    return answer