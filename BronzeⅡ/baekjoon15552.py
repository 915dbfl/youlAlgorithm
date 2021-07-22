#21.07.22
import sys
count = int(input())

for i in range(count):
  a, b = sys.stdin.readline().split(' ')
  print(int(a)+int(b))