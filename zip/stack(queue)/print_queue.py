#22.09.04
#프린터 큐
#class2_1
#queue

import sys
case = int(sys.stdin.readline())

for i in range(case):
  n , i = map(int, sys.stdin.readline().split())
  index = list(range(n))
  priority = list(map(int, sys.stdin.readline().split()))
  cnt = 0

  while 1:
    if priority[0] == max(priority):
      cnt += 1

      priority.pop(0)

      if index.pop(0) == i:
        print(cnt)
        break
    else:
      index.append(index.pop(0))
      priority.append(priority.pop(0))