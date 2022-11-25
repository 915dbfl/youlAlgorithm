#22.11.24
#곱셈
#class4/실버1
#분할 정복을 이용한 거듭제곱

# 시간 초과(O(n))
a, b, c = map(int, input().split())

print((a**b)%c)

# 반복문: 시간초과(O(logN))
import sys
def power(a, b):
  ans = 1
  while b > 0:
    if b%2:
      ans *= a
    a *= a
    b //= 2

  return ans%c

a, b, c = map(int, sys.stdin.readline().split())
print(power(a, b))

# 분할정복: 재귀로 구현(logN)
a, b, c = map(int, input().split())

def power(a, b, c):
  if b == 1:
    return a%c

  else:
    tmp = pow(a, b//2, c)

    if b % 2:
      return (a*tmp*tmp)%c
    else:
      return (tmp*tmp)%c

print(power(a, b, c))