#21.11.16
#그리디
import sys
N = int(sys.stdin.readline().rstrip())
lst = []
count = 0
for i in range(N):
  lst.append(list(map(int, sys.stdin.readline().rstrip().split())))
lst.sort(key= lambda i : (i[1], i[0]))

k, l = lst[0]
for j in range(1, N):
  n, o = lst[j]
  if n >= l:
    count += 1
    k, l = n, o

print(count + 1)