# 21.01.09
# 잃어버린 괄호

import sys

minus = list(sys.stdin.readline().rstrip().split('-'))
result = []

for i in minus:
  plus = list(map(int, i.split('+')))
  temp = 0
  for j in plus:
    temp += j

  result.append(temp)

for k in range(1, len(result)):
  result[0] -= result[k]

print(result[0])
  