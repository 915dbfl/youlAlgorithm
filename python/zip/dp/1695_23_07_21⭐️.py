#팰린드롬 만들기

#dp
#팰린드롬을 만들기 위해 최소 몇 개의 수를 끼워넣으면 되는지 파악
#LCS 최장 공통 부분 수열을 제외한 나머지를 끼워넣으면 되는 것!

import sys
n = int(input())
nums = list(map(int, input().split()))

dp = [[0] * (n+1) for _ in range(n+1)]

#dp를 이용해 최장 공통 부분 수열을 구하는 과정
for i in range(1, n+1): # reverse
    for j in range(1, n+1): # origin
        if nums[i-1] == nums[-j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

#전체 길이에서 최장 공통 부분 수열의 길이를 뺌
print(n - dp[-1][-1])


# 오답
# tmp1, tmp2 = 0, len(nums)-1
# cnt = 0
# while tmp1 <= tmp2:
#     if nums[tmp1] == nums[tmp2]:
#         tmp1 += 1
#         tmp2 -= 1
#     else:
#         if tmp2 == len(nums) - 1:
#             lst1 = nums[:]
#         else:
#             lst1 = nums[:tmp2+1]
#         cnt += 1
#         lst1 += [nums[tmp1]]
#         if tmp2 < len(nums) - 1:
#             nums = lst1 + nums[tmp2+1:]
#         else:
#             nums = lst1
#         tmp1 += 1

# print(cnt)