#22.12.29
#터렛
#알고리즘 스터디 2주차 -1

# 모든 예외 직접 처리
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  dis = (abs(x1-x2)**2+abs(y1-y2)**2)**0.5

  if x1 == x2 and y1 == y2:
    if r1 == r2:
      print(-1)
    else:
      print(0)
  else:
    tmp1 = max(r1, r2)
    tmp2 = dis + min(r1, r2)
    if tmp1 > tmp2:
      print(0)
    elif tmp1 == tmp2:
      print(1)
    else:
      if dis < r1+r2:
        print(2)
      elif dis == r1+r2:
        print(1)
      else:
        print(0)

#리팩토링
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  dis = (abs(x1-x2)**2+abs(y1-y2)**2)**0.5

  if dis == 0 and r1 == r2:
    print(-1)
  elif abs(r1-r2) == dis or r1+r2 == dis:
    print(1)
  elif abs(r1-r2) < dis < r1+r2:
    print(2)
  else:
    print(0)
