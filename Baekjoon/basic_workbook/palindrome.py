#2022.09.09
#소수&팬린드롬

#while 사용
import sys
n = int(input())

while 1:
  if n == 1:
    print(2)
    break
  else:
    tmp = str(n)
    if tmp == tmp[::-1]: # 팬린드롬인지 확인
      for i in range(2, int(n**0.5)+1): # 소수인지 확인
        if n % i == 0:
          n += 1
          break
      else: # 소수일 경우
        print(n)
        break
    else:
      n += 1

#for 사용
import sys
n = int(input())

for i in range(n, 1000001):
  if i == 1:
    print(2)
    break
  if i == 1000000:
    print(1003001)
    break
  tmp = str(i)
  if tmp == tmp[::-1]: # 팬린드롬인지 확인
    for j in range(2, int(i**0.5)+1): # 소수인지 확인
      if i % j == 0:
        break
    else: # 소수일 경우
      print(i)
      break