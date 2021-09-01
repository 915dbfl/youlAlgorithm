#21.09.01
num = int(input())
nums = list(map(int, input().split()))
for i in nums:
  if i == 1:
    num -= 1
  elif i != 2:
    for j in range(2,int(i**0.5)+1):
      if i % j == 0:
        num -= 1
        break
print(num)