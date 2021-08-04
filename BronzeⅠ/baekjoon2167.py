#21.08.04
import sys
n, m = map(int, input().split())
lst = []
for cnt in range(n):
  lst.append(list(map(int, sys.stdin.readline().split())))
k = int(input())
for cnt in range(k):
  total = 0
  i, j, x, y = map(int, sys.stdin.readline().split())
  for a in range(i-1, x):
    total += sum(lst[a][j-1:y])
  print(total)