import sys

def maxSum(sequence):
    l = len(sequence)
    INF = sys.maxsize
    dp = [0] * l
    Min = [INF] * l
    
    dp[0] = sequence[0]
    Min[0] = 0
    answer = -INF
    
    for i in range(1, l):
        dp[i] = dp[i-1] + sequence[i]
        Min[i] = Min[i-1]
        
        if dp[Min[i-1]] > dp[i]:
            Min[i] = i

        answer = max(dp[i] - dp[Min[i]], dp[i], answer)
        
    return answer
    
def solution(sequence):
    INF = sys.maxsize
    l = len(sequence)
    result = 0
    
    # sequence 길이 1
    if l == 1:
        return abs(sequence[0])
    
    # -1로 시작하는 펄스 수열 곱하기
    tmp = []
    perse = [-1, 1]
    for i in range(l):
        idx = (i%2)
        tmp.append(perse[idx] * sequence[i])

    result = max(maxSum(tmp), result)
    
    # 1로 시작하는 펄스 수열
    perse = [1, -1]
    tmp = []
    for i in range(l):
        idx = (i%2)
        tmp.append(perse[idx] * sequence[i])
        
    result = max(maxSum(tmp), result)
    
    return result

# 간단한 풀이
import sys

def solution(sequence):
    INF = sys.maxsize
    answer = -INF

    l = len(sequence)
    s1 = s2 = 0
    # 0으로 초기화해 -가 없을 경우에는 dp값이 answer의 후보가 되도록 한다.
    s1_min = s2_min = 0
    pulse = 1

    for i in range(l):
        s1 += sequence[i] * pulse
        s2 += sequence[i] * (-pulse)

        answer = max(answer, s1-s1_min, s2-s2_min)

        s1_min = min(s1_min, s1)
        s2_min = min(s2_min, s2)

        pulse *= -1

    return answer