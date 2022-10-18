#22.10.18
#회의실 배정
#class3/실버1

import sys
from collections import defaultdict

N = int(sys.stdin.readline())
dic = defaultdict(list)

for _ in range(N):
  s, e = map(int, sys.stdin.readline().split())
  dic[e].append(s)

for k in dic.keys():
  dic[k].sort()

answer = [0 for _ in range(max(dic.keys())+1)]

for i in range(len(answer)):
  for j in dic[i]:
    if i == j:
      answer[i] += 1
    else:
      answer[i] = max(answer[j]+1, answer[i])
  if i != 0:
    answer[i] = max(answer[i], answer[i-1])
    
print(answer[-1])