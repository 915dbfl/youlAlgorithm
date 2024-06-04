# dp 활용 정답
def solution(alp, cop, problems):
    max_alp_req, max_cop_req = [0, 0] # 목표값
    
    # 모든 문제를 풀기 위해 필요한 최소 목표값 구하기
    for problem in problems:
        max_alp_req = max(max_alp_req, problem[0])
        max_cop_req = max(max_cop_req, problem[1])
        
    dp = [[float('inf')] * (max_cop_req+1) for _ in range(max_alp_req+1)]
    
    alp = min(alp, max_alp_req)
    cop = min(cop, max_cop_req)
    
    dp[alp][cop] = 0
    
    for i in range(alp, max_alp_req+1):
        for j in range(cop, max_cop_req+1):
            # 알고력, 코딩력 1시간 학습하는 방식 적용
            if i < max_alp_req:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            if j < max_cop_req:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
                
            # 문제 푸는 방식 적용
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                # 풀 수 있는 문제인지 확인
                if i >= alp_req and j >= cop_req:
                    # 목표값을 넘는 경우도 목표값에 도달하는 방식 중 하나
                    new_alp = min(i+alp_rwd, max_alp_req)
                    new_cop = min(j+cop_rwd, max_cop_req)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + cost)
                    
    return dp[max_alp_req][max_cop_req]

# 내 풀이(시간 초과 + 오답)
from collections import deque

def solveP(target_alp, target_cop, alp, cop, solved):
    dq = deque([[alp, cop, 0]]) # 현재 alp, 현재 cop, 필요한 시간
    answer = [target_alp, target_cop, (abs(target_alp - alp) + abs(target_cop - cop))]
    
    while dq:
        ca, cc, t = dq.popleft()
        # print(ca, cc, t)
        
        if target_alp + target_cop <= ca + cc:
            if t < answer[2]:
                answer = [ca, cc, t]
            elif t == answer[2] and (answer[0] + answer[1]) < ca + cc:
                answer = [ca, cc, t]
            continue
            
        for pa, pc, pt in solved:
            dq.append([ca+pa, cc+pc, t+pt])
            
            re_alp = target_alp - (ca + pa)
            re_cop = target_cop - (cc + pc)
            if re_alp > 0 and re_cop > 0:
                dq.append([target_alp, target_cop, t+pt+re_alp+re_cop])
            
    return answer
            
def solution(alp, cop, problems):
    pl = len(problems)
    solved = set()
    time = 0
    
    while len(solved) < pl:
        # 풀 수 있는 문제 확인
        while 1:
            if alp < problems[0][0] or cop < problems[0][1]:
                # 알고력과 코딩력을 높임
                # 풀 문제가 없는 경우
                if len(solved) == 0:
                    time += problems[0][0] - alp
                    time += problems[0][1] - cop
                    alp, cop = problems[0][0], problems[0][1]
                # 풀 문제가 있는 경우
                else:
                    min_time, nalp, ncop = solveP(problems[0][0], problems[0][1], alp, cop, solved)
                    time += min_time
                    alp, cop = nalp, ncop
                break
            else:
                rm = problems.pop(0)
                solved.add((rm[2], rm[3], rm[4]))
        
        # 현재 알고력과 코딩력으로 해결 가능한 문제 순으로 정렬
        problems.sort(key = lambda x: (abs(alp - x[0]) + abs(cop - x[1])))
        
    return time