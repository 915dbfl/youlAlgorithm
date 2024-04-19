# dp
def getDp(dp, firstUsed, sticker):
    
    for i in range(2, len(sticker)-1):
        if dp[i-1] > dp[i-2] + sticker[i]:
            dp[i] = dp[i-1]
            firstUsed[i] = firstUsed[i-1]
        else:
            dp[i] = dp[i-2] + sticker[i]
            firstUsed[i] = firstUsed[i-2]

    dp[-1] = dp[-2]
    if not firstUsed[-3]:
        dp[-1] = max(dp[-1], dp[-3]+sticker[-1])
            
    return dp[-1]

def solution(sticker):
    if len(sticker) <= 2:
        return max(sticker)
    else:
        # 첫 번쨰 요소가 사용되는 경우 / 사용되지 않는 경우 모두 확인
        ## 1. 사용되는 경우
        dp = [0] * len(sticker)  
        firstUsed = [False] * len(sticker)
        firstUsed[0] = True
        
        # 0, 1번쨰 dp 초기화
        dp[0] = sticker[0]
        if sticker[0] > sticker[1]:
            dp[1] = sticker[0]
            firstUsed[1] = True
        else:
            dp[1] = sticker[1]
        
        # 첫 번째 요소가 사용될 떄 최대 값 가져오기
        answer = getDp(dp, firstUsed, sticker)
        
        # 2. 사용되지 않는 경우
        dp = [0] * len(sticker)  
        firstUsed = [False] * len(sticker)
        dp[1] = sticker[1]
        
        answer = max(answer, getDp(dp, firstUsed, sticker))

        return answer
    
# dp 간단한 풀이
def collect_sticker(sticker):
    dq = [0] * len(sticker)
    dq[0] = sticker[0]
    dq[1] = max(sticker[0], sticker[1])
    for i in range(2, len(sticker)):
        dq[i] = max(dq[i-1], dq[i-2] + sticker[i])

    return dq

def solution(sticker):
    if len(sticker) <= 2:
        return max(sticker)
    return max(collect_sticker(sticker[:-1])[-1],collect_sticker(sticker[1:])[-1])
