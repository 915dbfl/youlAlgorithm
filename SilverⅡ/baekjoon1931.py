#21.11.15
#그리디
import sys
N = int(sys.stdin.readline().rstrip())
lst = []
s = 0
count = 0
for i in range(11):
  lst.append(list(map(int, sys.stdin.readline().rstrip().split())))

lst.sort(key= lambda i : i[0])

while 1:
  if(s == N-1):
    count += 1
    break
  k, l = lst[s]
  for j in range(s+1, N):
    n, o = lst[j]
    if o <= l:
      k, l = n, o
    elif n >= l:
      s = j
      count += 1
      break

print(count)