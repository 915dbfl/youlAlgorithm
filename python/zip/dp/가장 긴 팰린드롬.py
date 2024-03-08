# dp

def solution(s):
    dp = [[-1] * len(s) for _ in range(len(s))]
    # 숫자 1개에 해당하는 dp, 1로 초기화
    for i in range(len(s)):
        dp[i][i] = 1
    answer = 1
    
    for i in range(len(s)): 
        for j in range(i):

            # s[i] == s[j]일 경우, dp 업데이트
            if i != j and s[i] == s[j]:
                if j + 1 == i:
                    dp[j][i] = 2
                elif dp[j+1][i-1] != -1:
                    dp[j][i] = max(dp[j][i], dp[j+1][i-1] + 2)
                answer = max(answer, dp[j][i])
    return answer