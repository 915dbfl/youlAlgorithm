#21.11.26
import sys
M, N = map(int, sys.stdin.readline().rstrip().split())

lst = [1 for _ in range(N+1)]
lst[1] = 0

for i in range(2, N):
  if lst[i] == 1:
    rng = N//i
    for j in range(2, rng+1):
      lst[i*j] = 0

for k in range(M, N+1):
  if lst[k] == 1:
    print(k)