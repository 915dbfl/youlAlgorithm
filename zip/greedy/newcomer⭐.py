#23.01.03
#신입사원
#알고리즘 스터디 3주차 -1
#실버1

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = int(input())
  lst = []

  for i in range(n):
    lst.append(list(map(int, input().split())))

  lst.sort()
  tmp = lst[0][1]
  answer = 1

  for i in range(1, n):
    if lst[i][1] < tmp:
      answer += 1
      tmp = lst[i][1]

  print(answer)