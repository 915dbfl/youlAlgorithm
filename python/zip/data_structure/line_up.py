#23.01.10
#줄 세우기
#알고리즘 스터디 4-2
#브론즈2

import sys
input = sys.stdin.readline

n = int(input())
lst = []
pick = list(map(int, input().split()))

for i, v in enumerate(pick):
  if v == 0:
    lst.append(str(i+1))
  else:
    lst.insert(len(lst)-v, str(i+1))

print(" ".join(lst))