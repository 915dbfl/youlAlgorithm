#21.08.15
import sys
num = int(input())
person = []
for i in range(num):
  person.append(list(map(int, sys.stdin.readline().rstrip().split())))
for i in person:
  count = 1
  for j in person :
    if j[0] > i[0] and j[1] > i[1]:
      count += 1
  print(count, end =" ")