#22.10.03
#제로
#class2/실버4
#queue

import sys

n = int(sys.stdin.readline())
que = []

for i in range(n):
  n = int(sys.stdin.readline())

  if n == 0:
    que.pop()
  else:
    que.append(n)

print(sum(que))