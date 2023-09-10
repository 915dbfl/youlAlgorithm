# 연속합2
# edge case:
    # 최소 하나는 선택되어야 한다.
    # dp의 값이 하나의 값으로 이루어져 있는 경우 따로 처리해야 함
import sys

n = int(input())
nums = list(map(int, input().split()))
dp = [0] * n
dp[0] = nums[0]
only = [False] * n
# 제거 없이 i번째 인덱스에서 얻을 수 있는 최대 연속된 수열의 합
# dp의 값이 nums의 값일 경우 only를 true로 세팅해준다.
for i in range(1, n):
    if dp[i-1] + nums[i] < nums[i]:
        dp[i] = nums[i]
        only[i] = True
    else:
        dp[i] = dp[i-1] + nums[i]

# i번째 연속된 수열의 최대합
    # only인지 아닌지에 따라 분기한다.
    # only일 경우
        # (앞에서 하나 제거한 최대 수열의 합 + nums[i])와 dp[i] 값 중 최대값을 선택
    # only가 아닐 경우
        # (아무것도 제거하지 않은 최대 수열의 합 - nums[i])와 (앞에서 하나 제거한 최대 수열의 합 + nums[i])값 중 최대값 선택
answer = [0]* n
answer[0] = dp[0]
for i in range(1, n):
    if only[i]:
        answer[i] = max(answer[i-1] + nums[i], dp[i])
    else:
        answer[i] = max(dp[i] - nums[i], answer[i-1] + nums[i])

print(max(answer))