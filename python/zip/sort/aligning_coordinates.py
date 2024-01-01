#22.10.05
#좌표 정렬하기
#class2/실버5
# 정렬

import sys

n = int(sys.stdin.readline())
coor = []

for i in range(n):
  coor.append(list(map(int, sys.stdin.readline().split())))

coor.sort(key = lambda x: (x[0], x[1]))

for j in coor:
  print(j[0], j[1])