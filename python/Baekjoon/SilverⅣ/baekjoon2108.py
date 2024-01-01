# 21.09.26
import sys
from collections import Counter

def mcount():
  global N, lst
  mcount_lst = Counter(lst).most_common(2)
  if len(mcount_lst) > 1:
    if mcount_lst[0][1] == mcount_lst[1][1]:
      print(mcount_lst[1][0])
    else:
      print(mcount_lst[0][0])
  else:
    print(mcount_lst[0][0])

N = int(sys.stdin.readline().rstrip())
lst = []
mcount_lst = []
for i in range(N):
  lst.append(int(sys.stdin.readline().rstrip()))
lst.sort()
print(round(sum(lst)/N))
print(lst[int(N/2)])
mcount()
print(lst[-1]-lst[0])