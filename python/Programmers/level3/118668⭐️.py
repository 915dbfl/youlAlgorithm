# 2022 카카오 인턴십 코딩테스트
# 코딩 테스트 공부
# dp

# 1시간 공부해 알고력, 코딩력을 +1씩 올릴 수 있음
# 문제에 맞는 시간을 공부해 알고력과 코딩력을 올릴 수 있음

# 이 두가지를 고려해 dp로 문제를 품

def solution(alp, cop, problems):
    # 모든 문제를 풀기 위해 필요한 알고력, 코딩력 최소값을 구한다.
    max_alp, max_cop  = alp, cop
    for problem in problems:
        max_alp = max(max_alp, problem[0])
        max_cop = max(max_cop, problem[1])
        
    # 목표 알고력, 코딩력
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    INF = float('inf')

    dp = [[INF] * (max_cop+1) for _ in range(max_alp+1)]
    dp[alp][cop] = 0 # 현재 알고력, 코딩력의 경우 드는 시간 0

    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop+1):
            if i < max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j < max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req: # 풀 수 있는 문제라면
                    # 최대 알고력, 코딩력을 넘지 않도록 설정
                    new_alp = min(i + alp_rwd, max_alp)
                    new_cop = min(j + cop_rwd, max_cop)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + cost)

    return dp[max_alp][max_cop]