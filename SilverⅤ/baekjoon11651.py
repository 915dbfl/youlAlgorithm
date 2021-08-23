#21.08.23
import sys
num = int(input())
nums = []
for i in range(num):
  nums.append(list(map(int, sys.stdin.readline().rsplit())))
nums.sort(key= lambda i :(i[1], i[0]))
for x, y in nums:
  print(x, y)