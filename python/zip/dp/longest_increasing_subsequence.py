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

#23.07.05
#가장 긴 증가하는 부분 수열

#dp
l = int(input())
lst = list(map(int, input().split()))
dp = [1 for _ in range(len(lst))]

for i in range(1, l):
    for j in range(i):
        if lst[j] < lst[i] and dp[i] < dp[j]+1:
            dp[i] = dp[j] + 1

print(max(dp))

#이해 안 감!
import sys

num_list = list(map(int, sys.stdin.readlines()[1].split()))
max_list = [0]
for num in num_list:
    if num > max_list[-1]:
        max_list.append(num)
    else:
        for idx in range(1, len(max_list)):
            if num <= max_list[idx]:
                max_list[idx] = num
                break
print(len(max_list)-1)