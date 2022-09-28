#22.09.28
#최대공약수와 최소공배수
#class2/브론즈1
#유클리드 호제법

#내 풀이
import math

a, b = map(int, input().split())

print(math.gcd(a, b))
print((a*b)//math.gcd(a, b))

#유클리드 호제법
def GCD(x, y):
  while(y):
    x, y = y, x%y
  return x

def LCM(x, y):
  return (x*y)//GCD(x, y)