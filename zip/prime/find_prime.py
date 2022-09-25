#22.09.25
#소수 찾기
#class2_1
#소수

N = int(input())

nums = list(map(int, input().split()))
cnt = 0

for i in nums:
  if i == 1:
    continue
  elif i == 2:
    cnt += 1
  else:
    for j in range(2, int(i**0.5)+1):
      if i % j == 0:
        break
    else:
      cnt += 1

print(cnt)