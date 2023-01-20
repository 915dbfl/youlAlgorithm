#23.01.20
#숨바꼭질2
#골드4

import sys
from collections import defaultdict, deque

def bfs(str):
  global min_sec
  dq = deque([[str, 0]])

  while dq:
    cur, sec = dq.popleft()

    if min_sec < k-n and sec > min_sec:
      break

    if cur == k:
      dic[sec] += 1
      if min_sec > sec:
        min_sec = sec
    else:
      if cur > k:
        if sec + cur - k <= min_sec:
          dic[sec+cur-k] += 1
      else:
        dq.append([cur-1, sec+1])
        dq.append([cur+1, sec+1])
        dq.append([cur*2, sec+1])

n, k = map(int, sys.stdin.readline().split())
dic = defaultdict(int)
min_sec = k-n

if min_sec <= 0:
  print(-min_sec)
else:
  bfs(n)
  print(min_sec)
  print(dic[min_sec])