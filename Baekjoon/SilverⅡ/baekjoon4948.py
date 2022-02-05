# 21.01.06
# 베르트랑 공준
import sys

result = [1 for i in range(246913)]
result[0] = 0

for i in range(2, 498):
  tmp = 246913 // i
  for j in range(2, tmp+1):
    if result[i*j] != 0:
      result[i*j] = 0

while 1:
  n = int(sys.stdin.readline().rstrip())
  if n == 0:
    break
  else:
    print(result[n+1:2*n+1].count(1))