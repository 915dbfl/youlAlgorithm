# 1시간 반 - greedy

"""
풀이과정
1. 유형별로 참가자 리스트 정리
2. 각 유형별로 멘토가 n명일 때 대기 시간 구하기
3. (x) 각 유형별로 멘토가 m명일 때 대기 시간 중 가장 긴 대기 유형에 멘토 + 1 (전체 대기 시간이 최소가 된다는 보장 x)
    - 최종멘토가 n명이 될 때까지 반복
3-1. (o) 각 유형별로 멘토가 +1 되었을 때 대기시간이 가장 많이 줄어드는 유형 선택
    - 최종멘토가 n명이 될 때까지 반복
4. 최종 결과 출력
"""
from heapq import heappush, heappop

def solution(k, n, reqs):
    # 멘토가 mentor_cnt명일 때 type 유형 대기시간 계산
    def cal_waiting_time(type, mentor_cnt):
        hq = []
        cur = 0
        size = len(types[type])
        waiting = 0
        for _ in range(mentor_cnt):
            start, duration = types[type][cur]
            heappush(hq, (start + duration))
            cur += 1
            
        while cur < size:
            cur_time = heappop(hq)
            nxt_start, nxt_duration = types[type][cur]
            cur += 1
            
            # 대기가 필요하면 대기
            if cur_time > nxt_start:
                waiting += cur_time - nxt_start
                nxt_start = cur_time
            
            # 상담 진행
            heappush(hq, nxt_start + nxt_duration)
            
        return waiting
        
    types = [[] for _ in range(k+1)]
    for a, b, c in reqs:
        types[c].append((a, b))
    
    # 각 유형별로 대기 시간 구하기
    waitings = [[0] * (n+1) for _ in range(k+1)]
    for type in range(1, k+1):
        min_mentor_cnt = min(len(types[type]), n)
        for mentor_cnt in range(1, min_mentor_cnt + 1):
            waitings[type][mentor_cnt] = cal_waiting_time(type, mentor_cnt)
            
    # 최소 대기 구하기
    # 각 유형별로 1명의 멘토는 존재해야 함
    mentors = [1] * (k+1)
    while (sum(mentors) - 1) < n:
        max_amount = waitings[1][mentors[1]] - waitings[1][mentors[1] + 1]
        max_type = 1
        
        # 멘토를 늘릴 유형 선택
        for i in range(2, k+1):
            mentor_cnt = mentors[i]
            amount = waitings[i][mentor_cnt] - waitings[i][mentor_cnt + 1]
            
            if max_amount < amount:
                max_amount = amount
                max_type = i
        
        mentors[max_type] += 1
        
    # 전체 대기 시간 계산
    answer = 0
    for i in range(1, k+1):
        answer += waitings[i][mentors[i]]
        
    return answer