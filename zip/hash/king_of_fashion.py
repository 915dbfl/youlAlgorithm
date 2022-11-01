#22.11.01
#패션왕 신해빈
#class3/실버3

import sys
from collections import defaultdict

t = int(sys.stdin.readline())

for _ in range(t):
  dic = defaultdict(list)
  n = int(sys.stdin.readline())

  for _ in range(n):
    i, category = sys.stdin.readline().split()
    dic[category].append(i)

  answer = 1
  for i in dic.keys():
    answer *= len(dic[i])+1

  print(answer-1)