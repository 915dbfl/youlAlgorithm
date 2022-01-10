# 21.01.10
# 4963: 섬의 개수

import sys
import copy

def getCheck(n, w):
  temp = copy.deepcopy(n)
  lst = []
  for i in range(w):
    if n[i] == 0:
      if i == 0 and w != 1 and n[i+1] == 1:
        temp[i] = 1
      elif i == w-1 and n[i-1] == 1:
        temp[i] = 1
      elif i != 0 and i != w-1:
        if n[i-1] == 1 and n[i+1] == 1:
          temp[i] = 2
        elif n[i-1] == 1 or n[i+1] == 1:
          temp[i] = 1
    elif n[i] == 3:
      lst.append(i)

  for j in lst:
    if j != 0 and j != w-1:
      temp[j-1] = 3
      temp[j+1] = 3
    elif j != 0:
      temp[j-1] = 3
    else:
      temp[j+1] = 3

  return temp

    

while 1:
  w, h = map(int,sys.stdin.readline().rstrip().split())
  if w == 0 and h == 0:
    break
  else:
    m = []
    for i in range(h):
      m.append(list(map(int, sys.stdin.readline().rstrip().split())))
  
    count = m[0][0]
    for i in range(w):
      if m[0][i] == 1:
        if i != 0 and m[0][i-1] != 1:
          count += 1

    check = getCheck(m[0], w)
    for j in range(1, h):
      ch  = m[j]
      for k in range(w):
        if m[j][k] == 1:
          if check[k] == 2:
            count -= 1
            ch[k] = 3
          elif check[k] == 0:
            count += 1
          if k != w-1 and check[k+1] == 0:
            check[k+1] = 1
          if check[k] == 3:
            ch[k] = 3
      check = getCheck(ch, w)

    print(count)