#21.08.23
import sys
n  = int(input())
lst = []
for i in range(n):
  lst.append(list(sys.stdin.readline().strip().split()))
lst.sort(key= lambda i: int(i[0]))
for i in lst:
  sys.stdout.write(i[0] + ' ' +  i[1] + '\n')
