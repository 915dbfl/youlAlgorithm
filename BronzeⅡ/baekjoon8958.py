#21.07.22
import sys
count = int(input())

for i in range(count):
  sum = 0
  countO = 0
  result = sys.stdin.readline().rstrip()
  for j in result:
    if j == 'O':
      countO += 1
      sum += countO
    else:
      countO = 0
  print(sum)
