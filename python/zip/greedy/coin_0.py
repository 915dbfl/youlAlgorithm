#22.11.03
#동전0
#class3/실버4

import sys

n, k = map(int, sys.stdin.readline().split())
coins = []

for _ in range(n):
  coins.append(int(sys.stdin.readline()))

coins.sort(reverse= True)

answer = 0
for c in coins:
  if c <= k:
    tmp = k // c
    answer += tmp
    k -= tmp*c
    if k == 0:
      break

print(answer)