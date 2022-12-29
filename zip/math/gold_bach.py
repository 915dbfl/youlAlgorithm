#22.12.29
#골드바흐의 추측
#알고리즘 스터디 2주차 -2
#실버1

import sys
input = sys.stdin.readline

def isPrime(n):
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      return False
  return True

t = int(input())

for _ in range(t):
  n = int(input())
  a = n//2
  b = n-a

  while 1:
    if isPrime(a) and isPrime(b):
      print(a, b)
      break
    else:
      a -= 1
      b += 1