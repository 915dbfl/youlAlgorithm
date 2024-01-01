#22.10.16
#듣보잡
#class3/실버4
#집합

import sys

N, M = map(int, sys.stdin.readline().split())

l_person = set()
s_person = set()

for _ in range(N):
  l_person.add(sys.stdin.readline().rstrip())

for _ in range(M):
  s_person.add(sys.stdin.readline().rstrip())

lst = sorted(list(l_person & s_person))
print(len(lst))
for p in lst:
  print(p)
