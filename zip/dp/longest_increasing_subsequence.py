#22.11.18
#가장 긴 증가하는 부분 수열
#class4/실버3
#dp

size = int(input())
nums = list(map(int, input().split()))
dp = [1]*size

for i in range(1, size):
  for j in range(i):
    if nums[i] > nums[j]:
      dp[i] = max(dp[i], dp[j]+1)

print(max(dp))