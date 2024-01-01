#22.11.03
#atm
#class3/실버4
#그리디

import sys

n = int(sys.stdin.readline())
times = list(map(int, sys.stdin.readline().split()))

times.sort()

tmp, answer = 0, 0
for t in times:
  answer += tmp+t
  tmp += t

print(answer)