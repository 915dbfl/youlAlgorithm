#22.01.03
#가장 긴 증가하는 부분 수열
import sys
l = int(input())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
result = [1 for i in range(l)]
max = 0

for i in range(1, l):
  m = 0
  if nums[i] > nums[i-1]:
    result[i] = nums[i-1] + 1
  else:
    for j in range(0, i):
      val = 0
      for k in range(j, i):
        if nums[k] < nums[k-1]:
          if nums[i] > nums[k] and nums[k] > val:
            result[i] += 1
            val = nums[k]
      if m < result[i]:
        m = result[i]
      result[i] = 1
    result[i] = m
  if max < result[i]:
    max = result[i]

print(max)

