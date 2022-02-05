# #21.07.28
import sys
num = int(input())
lst = []
for i in range(num):
  lst.append(int(sys.stdin.readline()))
for i in sorted(lst, reverse= False):
  print(i)