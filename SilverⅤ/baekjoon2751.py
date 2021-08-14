# #21.08.13
import sys
num = int(input())
lst = []
for i in range(num):
  lst.append(int(sys.stdin.readline().rstrip()))
for i in sorted(lst):
  sys.stdout.write(i)