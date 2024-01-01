# #21.09.03
import sys
n = int(input())
for i in range(n):
  ps = sys.stdin.readline().rstrip()
  sum = 0
  result = "NO"
  for j in ps:
    if j == "(":
      sum += 1
    else:
      sum -= 1
    if sum < 0:
      break
  if sum == 0: 
    result = "YES"
  print(result)