#21.09.18
import sys
num= int(input())
sum = p = 0
dtable = []
ptable = []
val= {}
for i in range(num):
  day, pay = map(int, sys.stdin.readline().rstrip().split())
  dtable.append(day)
  ptable.append(pay)


for j in range(num-1, -1, -1):
  # 맨 마지막인 경우
  if j == num-1:
    if dtable[j] == 1:
      p = ptable[j]
    else:
      p = 0
  # 맨 마지막이 아닌 경우
  else:
    # 수행 가능한 것
    if (dtable[j] + j) <= num:
      if (dtable[j] + j) == num:
        p1 = ptable[j]
      else:
        p1 = ptable[j] + val[j + dtable[j]]
      p2 = val[j+1]
      if p1 > p2:
        p = p1
      else:
        p = p2
    # 수행 불가능한 것
    else:
      p = val[j+1]
  val[j] = p 
print(val[0])