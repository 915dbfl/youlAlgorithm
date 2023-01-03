#23.01.03
#신입사원
#알고리즘 스터디 3주차 -1
#실버1

#시간초과
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = int(input())
  lst = []
  answer = 0

  for i in range(n):
    lst.append(list(map(int, input().split())))

  lst.sort(key = lambda x: x[0])

  for i in range(n):
    for j in range(i, n):
      if lst[i][1] > lst[j][1]:
        break
    else:
      answer += 1

  print(answer)