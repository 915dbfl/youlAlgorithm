#22.11.01
#1, 2, 3 더하기
#class3/실버3
#dp

import sys

t = int(sys.stdin.readline())

lst = [0, 1, 2, 4, 7, 13]

for _ in range(t):
  num = int(sys.stdin.readline())
  for i in range(5, num+1):
    lst.append(lst[-1] + lst[-2] + lst[-3])
  
  print(lst[num])