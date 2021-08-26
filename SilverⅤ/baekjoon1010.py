#21.08.24
import sys, math
num = int(input())
for i in range(num):
  n, m = map(int, sys.stdin.readline().rstrip().split())
  case = math.factorial(m) // (math.factorial(n) * math.factorial(m-n))
  print(case)