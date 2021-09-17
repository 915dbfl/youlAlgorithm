#21.09.17
import sys
num = int(sys.stdin.readline().rstrip())
buf = []
for i in range(num):
  n = int(sys.stdin.readline().rstrip())
  if n != 0:
    buf.append(n)
  else:
    buf.pop()
print(sum(buf))