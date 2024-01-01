#21.09.29
import sys
N = int(input())
w_lst = []
max = 0
for i in range(N):
  w_lst.append(int(sys.stdin.readline().rstrip()))
w_lst.sort()
for i in range(N):
  temp = w_lst[i]*(N-i)
  if max < temp:
    max = temp
print(max)