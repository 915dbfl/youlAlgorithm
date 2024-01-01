#22.09.24
#소수 구하기
#class2_1
#에라토스테네스의 체(소수), 차집합

from collections import defaultdict
import sys

M, N = map(int, sys.stdin.readline().split())

s = set([i for i in range(2, N+1)])

for i in range(2, int(N**0.5)+1):
  if i in s:
    tmp = set([j for j in range(i*2, N+1, i)])
    s -= tmp

for i in range(M, N+1):
  if i in s:
    sys.stdout.write(str(i)+"\n")