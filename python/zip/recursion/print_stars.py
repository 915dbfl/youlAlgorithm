#23.01.11
#별 찍기
#골드 4

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
size = n*2-1
lst = [[" " for _ in range(size)] for _ in range(n)]

q = deque([[0, size//2]])

while q:
  x, y = q.popleft()
  if x > 0 and lst[x-1][y-1] == "*" and lst[x-1][y+1] == "*":
    continue

  #삼각형 꼭대기
  lst[x][y] = "*"
  #삼각형 가운데
  lst[x+1][y-1] = "*"
  lst[x+1][y+1] = "*"
  #삼각혁 밑변
  for i in range(5):
    lst[x+2][y-2+i] = "*"
  
  if x+2 < n-1:
    q.append([x+3, y-3]) 
    q.append([x+3, y+3])
    
for line in lst:
  print("".join(line))

# 리팩터링
figures = dict()
figures[3] = ['  *  ', ' * * ', '*****']

for k in range(1, 11):
  tmp = []
  for line in figures[3*2**(k-1)]:
    tmp.append(' '*(3*2**(k-1)) + line + ' '*(3*2**(k-1)))
  for i in range(3*2**(k-1)):
    tmp.append(figures[3*2**(k-1)][i] + ' ' + figures[3*2**(k-1)][i])
  figures[3*2**k] = tmp

print("\n".join(figures[int(input())]))

# 재귀 사용하기
n = int(input())
graph = [[" " for _ in range(n*2-1)] for _ in range(n)]

def recursion(x, y, N):
  if N == 3:
    graph[x][y] = "*"
    graph[x+1][y-1] = graph[x+1][y+1] = "*"
    for i in range(-2, 3):
      graph[x+2][y+i] = "*"
  else:
    nN = N//2
    recursion(x, y, nN)
    recursion(x+nN, y-nN, nN)
    recursion(x+nN, y+nN, nN)

recursion(0, n-1, n)
for i in graph:
  print("".join(i))

# 재귀 사용하기-2
n = int(input())

def recursion(k):
  if k == 3:
    return ["  *  ", " * * ", "*****"]

  result = []
  unit = recursion(k//2)

  for i in range(k):
    if i < k//2:
      result.append(" "*(k//2) + unit[i] + " "*(k//2))
    else:
      result.append(unit[i-k//2] + " " + unit[i-k//2])

  return result

print("\n".join(recursion(n)))