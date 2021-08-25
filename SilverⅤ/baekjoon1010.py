#21.08.24
import sys
num = int(input())
cases = []
for i in range(num):
  cases.append(list(map(int, sys.stdin.readline().rstrip().split())))
for n, m in cases:
  dif = m-n+1
  lst = []
  if n ==1:
    print(m)
  elif n == m:
    print(1)
  else:
    for i in range(n-2+1):
      if i == 0:
        lst = [i for i in range(1, dif+1)]
      else:
        lst = [sum(lst[0:i+1]) for i in range(0, dif) if lst]
    print(sum(lst))