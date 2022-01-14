# # 21.01.11
# # 6603: 로또

import itertools, sys

while 1:
  lst = list(sys.stdin.readline().rstrip().split())
  k = int(lst[0])
  if k == 0:
    break

  result = list(itertools.combinations(lst[1:], 6))
  for i in result:
    print(" ".join(i))

  print()
