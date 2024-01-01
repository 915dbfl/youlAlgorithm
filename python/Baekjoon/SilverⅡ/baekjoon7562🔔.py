#21.01.20
#7562: 나이트의 이동

import sys
sys.setrecursionlimit(10000)

num = int(sys.stdin.readline())
lst = [[-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2]]

def check(start, end, k):
  if k[0] > 0 and k[1] > 0:
    if end[0] >= start[0] and end[1] >= start[1]:
      return True
  elif k[0] > 0 and k[1] < 0:
    if end[0] >= start[0] and end[1] <= start[1]:
      return True
  elif k[0] < 0 and k[1] > 0:
    if end[0] <= start[0] and end[1] >= start[1]:
      return True
  elif k[0] < 0 and k[1] < 0:
    if end[0] <= start[0] and end[1] <= start[1]:
      return True
  return False
    

def bfs(start, end):
  global count, chk

  queue = [[start[0], start[1], 0]]

  while queue:
    if chk == 1:
      return

    a, b, c = queue[0][0], queue[0][1], queue[0][2]
    del queue[0]

    if a == end[0] and b == end[1]:
      print(c)
      chk = 1

    else:
      for k in lst:
        if(check([a,b], end, k)):
          x = a + k[0]
          y = b + k[1]
          z = c + 1
          queue.append([x, y, z])


    
for _ in range(num):
  l = int(sys.stdin.readline())
  start = list(map(int,sys.stdin.readline().rstrip().split()))
  end = list(map(int, sys.stdin.readline().rstrip().split()))
  chk = 0
  count = 0
  bfs(start, end)