#22.12.05
#이진 검색 트리
#class4/골드5
#이분탐색

## 트리 형성 + 후위 순회
import sys
sys.setrecursionlimit(10**6)

#후위 순회
def postOrder(root):
  left, right = 0, 0
  left, right = dic[root]
  
  if left != -1:
    postOrder(left)
  if right != -1:
    postOrder(right)
  print(root)

# 오른쪽 요소의 부모노트 찾기
def findParent(n, lst):
  cur = -1

  while 1:
    if len(lst) == 0 or lst[-1] > n:
      break
    else:
      cur = lst.pop()
      
  return cur
  
root = int(sys.stdin.readline())
lst = [root]
dic = {}
dic[root] = [-1, -1]

#트리 구조 파악
while 1:
  try:
    n = int(sys.stdin.readline())
    dic[n] = [-1, -1]
  except:
    break

  if n < lst[-1]:
    dic[lst[-1]] = [n, -1]
    lst.append(n)

  elif n > lst[-1]:
    p = findParent(n, lst)
    dic[p][1] = n
    lst.append(n)

postOrder(root)

## 이분탐색
import sys
sys.setrecursionlimit(10**6)

def postOrder(s, e):
  if s > e:
    return
  
  mid = e+1
  for i in range(s+1, e+1):
    if lst[s] < lst[i]:
      mid = i
      break
  
  postOrder(s+1, mid-1)
  postOrder(mid, e)
  print(lst[s])
  
lst = []
while 1:
  try:
    n = int(sys.stdin.readline())
    lst.append(n)
  except:
    break

postOrder(0, len(lst)-1)

## 이분탐색: bisect 모듈 사용하기
import sys
sys.setrecursionlimit(10**6)
from bisect import bisect_right

def postOrder(s, e):
  if s == e:
    return
  
  mid = bisect_right(lst, lst[s], s, e)
  
  postOrder(s+1, mid)
  postOrder(mid, e)
  print(lst[s])
  
lst = []
while 1:
  try:
    n = int(sys.stdin.readline())
    lst.append(n)
  except:
    break

postOrder(0, len(lst))