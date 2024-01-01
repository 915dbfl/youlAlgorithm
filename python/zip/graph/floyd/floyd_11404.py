#23.01.19
#플로이드
#골드4

import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = sys.maxsize

cost = [[INF]*n for _ in range(n)]

for _ in range(m):
  a, b, c = map(int, sys.stdin.readline().split())
  cost[a-1][b-1] = min(cost[a-1][b-1], c)

for k in range(n):
  for i in range(n):
    for j in range(n):

      if i == j:
        cost[i][j] = 0
        continue

      if cost[i][j] > cost[i][k] + cost[k][j]:
        cost[i][j] = cost[i][k] + cost[k][j]

for c in cost:
  for e in c:
    if e >= INF:
      print(0, end = " ")
    else:
      print(e, end = " ")
  print()