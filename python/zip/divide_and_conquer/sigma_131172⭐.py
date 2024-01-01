#23.01.25
#시그마
#골드4

#분할정복
# b^(x-2) = b^(-1) mod x
# b^(-1) = b^(x-2) mod x
# 따라서 b^1000000005의 거듭제곱을 O(logN)의 효율로 구하기 위해 분할정복 사용
import sys
from math import gcd

def divideAndConquer(b, n): # 분할정복(O(logN))
  if n == 0:
    return 1
  
  else:
    tmp = divideAndConquer(b, n//2) % 1000000007
    
    if n % 2: # 홀수
      return (tmp*tmp*b) % 1000000007
    else: # 짝수
      return tmp*tmp % 1000000007

m = int(sys.stdin.readline())
answer = 0

for _ in range(m):
  b, a = map(int, sys.stdin.readline().split())
  g = gcd(a, b) # 최대공약수
  # 최대공약수로 나눠 기약분수 구함
  b //= g 
  a //= g

  answer += (a*divideAndConquer(b, 1000000005)) % 1000000007
  answer %= 1000000007

print(answer)