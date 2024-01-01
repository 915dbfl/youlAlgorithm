#21.09.22
import sys
N = int(sys.stdin.readline().rstrip())
A = set(sys.stdin.readline().rstrip().split())
M = int(sys.stdin.readline().rstrip())
B = list(sys.stdin.readline().rstrip().split())
for i in B:
  if i in A:
    sys.stdout.write("1\n")
  else:
    sys.stdout.write("0\n")