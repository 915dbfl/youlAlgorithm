# 병사 배치하기

# dp, LIS(longest increasing subsequence)
# 각 위치까지 병사가 포함될 때 최대 병사수
# 전체 - 가장 긴 증가하는 부분 수열의 길이

n = int(input())
powers = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i-1, -1, -1):
        if powers[j] > powers[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))