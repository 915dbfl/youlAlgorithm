# n개의 괄호를 사용해 올바른 괄호를 만드는 방법
# 괄호의 개수 구하기 = 카탈란 수열
# Cn = ΣCiC(n-i) (i = 0 ~ n)
    #  ex) C4 = C0C3 + C1C2 + C2C1 + C3C0

def solution(n):
    dp = [0] * (n+1)
    # 곰셈을 위해 1로 초기화
    dp[0] = 1

    for i in range(1, n+1):
        for j in range(i):
            dp[i] += dp[j] * dp[i-j-1]
    
    return dp[n]