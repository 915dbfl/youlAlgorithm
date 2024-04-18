# napsack 알고리즘
# dp[i][j] -> 동전 i를 이용해 금액 j를 만들 수 있는 방법
    # += dp[i-1][j-값] 
    # dp[i][j+값] += dp[i][j]

def solution(n, money):
    type = len(money)
    dp = [[0]*(n+1) for _ in range(type)]

    # dp 0번째 배열 초기화
    cnt = 0
    while money[0] * cnt <= n:
        dp[0][money[0]*cnt] += 1
        cnt += 1
    
    # dp 진행
    for i in range(1, type):
        amount = money[i]
        
        for j in range(n+1):
            dp[i][j] += dp[i-1][j] % 1000000007
            # 화폐 가격보다 작을 경우
            if j >= amount:
                dp[i][j] += dp[i-1][j-amount] % 1000000007
                
                if j+amount <= n:
                    dp[i][j+amount] += (dp[i][j] - dp[i-1][j])


    return dp[-1][-1] % 1000000007

# 정말 간단한 dp 풀이
def solution(n, money):
    dp = [0] * (n+1)
    dp[0] = 1

    for typ in money:
        for price in range(typ, n+1):
            dp[price] += dp[price - typ]
            dp[price] %= 1000000007

    return dp[-1]