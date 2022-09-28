#22.09.28
#나무 자르기
#class2/실버2
#이분탐색(binary search)

import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

s = 1
e = max(trees)

while s <= e:
  mid = (s+e)//2
  cnt = 0

  for i in trees:
    if i > mid:
      cnt += i - mid

  if cnt >= M:
    s = mid + 1
  else:
    e = mid - 1

print(e)