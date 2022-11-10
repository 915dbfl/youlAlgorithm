# 22.11.01
# DSLR
# class3/골드4
# bfs: 최단거리

import sys
from collections import deque, defaultdict

t = int(sys.stdin.readline())

def bfs(srt, end):
  dq = deque([[srt, ""]])
  visited = defaultdict(int)
  visited[srt] += 1

  while dq:
    val, t= dq.popleft()
      
    new_num = val-1 if val > 0 else 9999
    if new_num == end:
      print(t+"S")
      return
    elif visited[new_num] == 0:
      dq.append([new_num, t+"S"])
      visited[new_num] += 1

    new_num = val*2 if val*2 < 9999 else val*2%10000
    if new_num == end:
      print(t+"D")
      return
    elif visited[new_num] == 0:
      dq.append([new_num, t+"D"])
      visited[new_num] += 1

    new_num = (val % 1000) * 10 + val // 1000
    if new_num == end:
      print(t+"L")
      return
    elif visited[new_num] == 0:
      dq.append([new_num, t+"L"])
      visited[new_num] += 1

    new_num = (val % 10) * 1000 + val // 10
    if new_num == end:
      print(t+"R")
      return
    elif visited[new_num] == 0:
      dq.append([new_num, t+"R"])
      visited[new_num] +=1 

for _ in range(t):
  srt, end = map(int, sys.stdin.readline().split())
  bfs(srt, end)