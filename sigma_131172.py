#23.01.25
#시그마
#골드4

#오답
import sys
from math import gcd

def lcm(a, b):
  return a*b // gcd(a, b)

def sigma(a, b):
  tmp = 1000000007
  
  inverse = lcm(tmp+1, b) // b
  return (a*inverse)%tmp

m = int(sys.stdin.readline())
answer = 0

for _ in range(m):
  a, b =  map(int, sys.stdin.readline().split())
  answer += sigma(b, a)

print(answer)