#21.09.01
#소수 찾기: 에라토스테네스의 체 사용
num = int(input())
nums = list(map(int, input().split()))
end = max(nums)
count = 0
lst = [i for i in range(2, end + 1)]
for i in range(2, int(end ** 0.5)+1):
  if i in lst:
    for j in range(i*2, end+1, i):
      if j in lst:
        lst.remove(j)

for i in nums:
  if i in lst:
    count+= 1
print(count)