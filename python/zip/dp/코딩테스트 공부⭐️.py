# dp 활용 정답
# 재풀이(40분)
import sys

def solution(alp, cop, problems):
    # 구해야 하는 max 값들 계산
    maxAlp, maxCop = 0, 0
    for problem in problems:
        maxAlp = max(maxAlp, problem[0])
        maxCop = max(maxCop, problem[1])
        
    alp = min(alp, maxAlp)
    cop = min(cop, maxCop)
    
    # dp 초기화    
    dp = [[sys.maxsize] * (maxCop+2) for _ in range(maxAlp+2)]
    
    # 현재 상태로도 얻을 수 있는 알고력 / 코딩력 체크
    for i in range(alp+1):
        for j in range(cop+1):
            dp[i][j] = 0
            
    # 점화식 진행
    for i in range(alp, maxAlp+1):
        for j in range(cop, maxCop+1):
            # 공부할 경우
            dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            # 풀 수 있는 문제 풀기
            for problem in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
                # 풀 수 있는 문제라면
                if i >= alp_req and j >= cop_req:
                    nalp = min(i+alp_rwd, maxAlp)
                    ncop = min(j+cop_rwd, maxCop)
                    dp[nalp][ncop] = min(dp[nalp][ncop], dp[i][j] + cost)
                    
    return dp[maxAlp][maxCop]

# heapq를 사용한 풀이
from heapq import heappush, heappop

def solution(alp, cop, problems):
    max_alp = max(x[0] for x in problems)
    max_cop = max(x[1] for x in problems)
    table = [[int(1e9) for _ in range(151)] for _ in range(151)]
    problems += [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]

    h = [(0, alp, cop)]
    table[alp][cop] = 0

    while h:
        cur_cost, cur_alp, cur_cop = heappop(h)
        if cur_alp >= max_alp and cur_cop >= max_cop:
            return cur_cost
        
        if table[cur_alp][cur_cop] <= cur_cost:
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                n_alp = min(150, cur_alp + alp_rwd)
                n_cop = min(150, cur_cop + cop_rwd)
                # 풀 수 있는 문제라면
                if cur_alp >= alp_req and cur_cop >= cop_req and cur_cost + cost <= table[n_alp][n_cop]:
                    table[n_alp][n_cop] = cur_cost + cost
                    heappush(h, (cur_cost + cost, n_alp, n_cop))