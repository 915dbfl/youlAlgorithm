#21.08.24
import math
num = input()
nums = [0]*9
for i in num:
  if i == '6' or i == '9':
    nums[6] += 1
  else:
    nums[int(i)] += 1
nums[6] = math.ceil(nums[6] / 2)
print(max(nums))