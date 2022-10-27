#22.10.27
#카잉달력
#class3/실버1
#최소공배수, 최대공약수

from math import gcd
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
  m, n, x, y = map(int, input().split())

  tmp = m*n // gcd(m, n)
  for i in range(tmp//m):
    if (m*i+x) % n == y%n:
      print(m*i+x)
      break
  else:
    print(-1)

# 다른 풀이: https://www.acmicpc.net/source/50010793