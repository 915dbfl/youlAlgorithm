#21.11.14
#그리디 알고리즘
import sys
N, K = map(int, input().split())
lst = []
idx = 0
count = 0
for i in range(N):
  lst.append(int(sys.stdin.readline().rstrip()))

lst.sort(reverse=True)

while(K > 0):
  if lst[idx] <= K:
    count += K // lst[idx]
    K -= lst[idx] * (K//lst[idx])
  idx += 1

print(count)