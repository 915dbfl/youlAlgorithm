# 근무 태도 점수, 동료 평가 점수 -> 다른 사원보다 두 점수가 모두 낮은 경우가 한 번이라도 존재
# 인센티브 x

# 두 점수의 합이 높은 순
# 동석차의 수만큼 다음 석차 건너뜀
# 원호의 석차, 인센티브 받지 못하면 -1

def solution(scores):
    # 인덱스와 함께 저장
    scroeWithIdx = []
    for idx, score in enumerate(scores):
        scroeWithIdx.append([idx, score])
    
    # 근무 태도 점수 내림차순 정렬
    # 동료 평가 점수 오름차순 정렬 ⭐️
    # 둘다 내림차순 정렬할 시 반례: [100,2],[100,1],[50,1]
    scroeWithIdx.sort(key = lambda x: (x[1][0], -x[1][1]), reverse = True)

    dp = [-1] * len(scores) # 넘어야하는 최소 동료 평가 점수값
    dp[0] = scroeWithIdx[0][1][1]
    
    rank = [[scroeWithIdx[0][0], sum(scroeWithIdx[0][1])]]
    for i in range(1, len(scores)):
        idx, tmpS = scroeWithIdx[i]
        tmpT = sum(tmpS)
        # 석차에서 제외
        if dp[i-1] > tmpS[1]:
            if idx == 0:
                return -1  
        # 석차에 포함
        else:
            rank.append([idx, tmpT])
        dp[i] = max(dp[i-1], tmpS[1])
            
    # 합에 대한 내림차순
    rank.sort(key = lambda x: -x[1])
    r = 0
    n = 0
    for i in range(len(rank)):
        if i == 0:
            r = n+1
            n += 1
        else:
            # 동점이라면
            if rank[i-1][1] == rank[i][1]:
                n += 1
            # 동점이 아니라면
            elif rank[i-1][1] > rank[i][1]:
                r = n+1
                n += 1

        if rank[i][0] == 0:
            return r
        
# 다른 풀이
def solution(scores):
    wanho = scores[0]
    wanho_sum = sum(wanho)
    # 근무 평가 내림, 동료 평가 오름
    scores.sorT(key = lambda s: (-s[0], s[1]))
    max_company, answer = 0, 1
    
    for s in scores:
        if wanho[0] < s[0] and wanho[1] < s[1]:
            return -1
        
        # 직전보다 동료 평가가 크거나 같다면 -> 석차에 포함⭐️
        if max_company <= s[1]:
            if wanho_sum < s[0] + s[1]:
                answer += 1
            max_company = s[1] # 높은 동료 평가 저장