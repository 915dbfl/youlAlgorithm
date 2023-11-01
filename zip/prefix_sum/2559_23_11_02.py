# 수열
# 누적합

# 초반 0으로 셋팅했기 때문에 k-1 ~ 값 중 최대를 고르도록 해야 함

n, k = map(int, input().split())
nums = list(map(int, input().split()))

dp = [0]*(n)
dp[k-1] = sum(nums[:k])

for i in range(k, n):
    dp[i] = dp[i-1] + nums[i] - nums[i-k]

print(max(dp[k-1:]))