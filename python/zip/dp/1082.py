# dp
n = int(input())
price = list(map(int, input().split()))
m = int(input())
dp = [-1] * (51) # dp[i] -> i원을 가지고 만들 수 있는 가장 큰 방 번호

# dp 초기값 세팅
for i in range(n):
    dp[price[i]] = i

# dp값 구하기
for i in range(min(price) + 1, m+1):
    dp[i] = max(dp[i-1], dp[i])
    for j in range(n):
        dif = i - price[j]
        if dif > 0 and dp[dif] not in [-1, 0]:
            dp[i] = max(int(str(dp[dif]) + str(j)), dp[i])

print(dp[m])