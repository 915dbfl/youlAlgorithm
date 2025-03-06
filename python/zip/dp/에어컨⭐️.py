# 시간 초과

"""
주요 정보
- 초기 실내 = 실외 온도
- 에어컨 on: 1분 후 실내 온도 + / - 1 (희망온도 방향)
    - 실내 != 희망 -> 매분 a 전력
    - 실내 == 희망 -> 매분 b 전력
- 에어컨 off: 1분 후 실내 온도 + / - 1 (실내온도 방향)
- t1 ~ t2도 사이 유지하며 소비 전력 최소화

# 승객 탑승 중 쾌적한 실내온도 유지를 위한 최소 소비 전력?
- 경우의 수
    - 희망 온도를 높게 잡고, 계속 유지
    - 희망 온도를 낮게 잡고, 틀었다가 끄기
    - 손님이 없을 때 에어컨을 끄기
    - 손님이 없을 때 희망온도 유지하기
- dfs로 진행
"""

import sys
from collections import deque

def solution(temperature, t1, t2, a, b, onboard):
    def check_temp(time, temp):
        return (onboard[time] == 1 and t1 <= temp <= t2) or onboard[time] == 0
    
    start_time = -1
    for i in range(len(onboard)):
        if onboard[i] == 1:
            start_time = i
            break
            
    dq = deque()
    isHot = temperature > t2
    init_walt = a * (temperature - t2) if isHot else (t1 - temperature) * a
    init_temp = t2 if isHot else t1
    # 시간, 현재 온도, 사용 전력
    dq.append((i, init_temp, init_walt))
    answer = sys.maxsize
    
    while dq:
        time, temp, walt = dq.pop()
        
        if answer <= walt:
            continue
            
        if onboard[time] == 1 and (temp < t1 or temp > t2):
            continue
            
        if time == len(onboard) - 1:
            answer = min(walt, answer)
            continue

        # 현재 온도를 유지하거나
        nxt_time = time
        need_walt = 0
        status = onboard[time]
        while (nxt_time <= len(onboard) - 2) and onboard[nxt_time] == status:
            need_walt += b
            nxt_time += 1

        dq.append((nxt_time, temp, walt + need_walt))

        # 더 낮추거나
        diff = -1 if isHot else +1
        if check_temp(time + 1, temp + diff):
            dq.append((time + 1, temp + diff, walt + a))
            
        # 안 틀거나
        if check_temp(time+1, temp - diff):
            dq.append((time + 1, temp - diff, walt))
            
    return answer


# dp 적용
"""
주요 정보
- 초기 실내 = 실외 온도
- 에어컨 on: 1분 후 실내 온도 + / - 1 (희망온도 방향)
    - 실내 != 희망 -> 매분 a 전력
    - 실내 == 희망 -> 매분 b 전력
- 에어컨 off: 1분 후 실내 온도 + / - 1 (실내온도 방향)
- t1 ~ t2도 사이 유지하며 소비 전력 최소화

# 승객 탑승 중 쾌적한 실내온도 유지를 위한 최소 소비 전력?
- 경우의 수
    - 희망 온도를 높게 잡고, 계속 유지
    - 희망 온도를 낮게 잡고, 틀었다가 끄기
    - 손님이 없을 때 에어컨을 끄기
    - 손님이 없을 때 희망온도 유지하기
"""
"""
# 승객 탑승 중 쾌적한 실내온도 유지를 위한 최소 소비 전력?
- 경우의 수
    - 에어컨 x, 실내 != 실외 -> 온도 변화
    - 에어컨 x, 실내 == 실외 -> 온도 변화x
    - 에어컨 o, 실내 != 희망 -> 온도 변화
    - 에어컨 o, 실내 == 희망 -> 온도 유지
"""

def solution(temperature, t1, t2, a, b, onboard):
    max_walt = 1000 * 100
    t1 += 10
    t2 += 10
    temperature += 10
    
    # DP[i][j] : i분에 j 온도를 만들 수 있는 가장 적은 전력
    dp = [[max_walt] * 51 for _ in range(len(onboard))] 
    dp[0][temperature] = 0
    
    # 에어컨 온도 방향 
    temp_diff = -1 if temperature > t2 else 1
 
    for i in range(1, len(onboard)):
        for j in range(51):
            if (onboard[i] == 1 and t1 <= j <= t2) or onboard[i] == 0:
                # 에어컨 x, 실내 != 실외
                if 0 <= j+temp_diff <= 50 :
                    dp[i][j] = min(dp[i][j], dp[i-1][j+temp_diff])
                # 에어컨 x, 실내 == 실외
                if j == temperature:
                    dp[i][j] = min(dp[i][j], dp[i-1][j])
                # 에어컨 o, 온도 변화 o
                if 0 <= j-temp_diff <= 50:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-temp_diff] + a)
                # 에어컨 o, 온도 변화 x(희망 == 현재 온도)
                if t1 <= j <= t2:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + b)
            
    answer = min(dp[len(onboard)-1])
    return answer