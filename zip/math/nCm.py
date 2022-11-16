#22.11.16
#조합
#class4/실버3
#수학: 팩토리얼

from math import factorial

def useModule(n, m): # math 모듈 사용하기
  return factorial(n)//(factorial(m)*factorial(n-m))

def factorial(n): # 재귀 사용하기
  tmp = 1
  for i in range(2, n+1):
    tmp *= i
  return tmp

n, m = map(int, input().split())

print(factorial(n)//(factorial(m)*factorial(n-m)))
print(useModule(n, m))