# 1학년

# bfs: 메모리 초과
from collections import deque

n = int(input())
nums = list(map(int, input().split()))

def bfs():
    dq = deque()
    dq.append((0, 0)) # index, sum
    
    answer = 0
    while dq:
        idx, sum = dq.popleft()

        if idx == len(nums)-1:
            if sum == nums[idx]:
                answer += 1
                continue

        if sum - nums[idx] >= 0:
            dq.append((idx+1, sum - nums[idx]))
        if sum + nums[idx] <= 20:
            dq.append((idx+1, sum + nums[idx]))

    return answer

print(bfs())

# dp
# dp[i][j]: i번째 떄 j값이 되는 방법수
n = int(input())
nums = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(n-1)]

dp[0][nums[0]] = 1 
for i in range(n-1): #idx가 i일 때 
    for j in range(21):
        if j-nums[i] >= 0:
            dp[i][j] += dp[i-1][j-nums[i]]
        if j+nums[i] <= 20:
            dp[i][j] += dp[i-1][j+nums[i]]

print(dp[-1][nums[-1]])