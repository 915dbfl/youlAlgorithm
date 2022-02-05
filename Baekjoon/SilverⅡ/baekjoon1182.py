#21.01.12
#1182: 부분수열의 합

import sys

def dfs(index, sum):
  global count
  if index >= N:
    return
  sum += lst[index]
  if sum == S:
    count += 1
  dfs(index + 1, sum)
  dfs(index + 1, sum - lst[index])

N, S = map(int, sys.stdin.readline().rstrip().split())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
count = 0
dfs(0, 0)
print(count)