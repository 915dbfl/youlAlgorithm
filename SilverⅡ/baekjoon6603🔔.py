# 21.01.11
# 6603: 로또

from copy import deepcopy
from ntpath import join
import sys
sys.setrecursionlimit(10000)

def dfs(i, queue):
  q = deepcopy(queue)
  q.append(lst[i])
  if len(q) == 6:
    print(" ".join(q))
    return
  else:
    for j in range(i+1, k-(6-len(q))+1):
      dfs(j, q)

while 1:
  lst = list(sys.stdin.readline().rstrip().split())
  k = int(lst[0])
  if k == 0:
    break

  lst = lst[1:]
  for i in range(0, k-5):
    queue = []
    dfs(i, queue)
  print("\n", end="")


