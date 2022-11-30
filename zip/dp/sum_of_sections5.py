#22.11.30
#구간 합 구하기5
#class4/실버1
#dp

import sys

def dp():
  for i in range(n):
    for j in range(n):
      if i == 0 and j == 0:
        continue

      if i == 0:
        lst[i][j] +=  lst[i][j-1]
      elif j == 0:
        lst[i][j] += lst[i-1][j]
      else:
        lst[i][j] += (lst[i][j-1] + lst[i-1][j] - lst[i-1][j-1])

n, m = map(int, sys.stdin.readline().split())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp()

for _ in range(m):
  x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

  ans = lst[x2-1][y2-1]

  if y1 > 1:
    ans -= lst[x2-1][y1-2]
  if x1 > 1:
    ans -= lst[x1-2][y2-1]
  if x1 > 1 and y1 > 1:
    ans += lst[x1-2][y1-2]
  
  print(ans)