#22.10.22
#AC
#class3/골드5
#queue


# 'R'에서 revrse를 할 경우, 시간초과가 발생! -> O(N)
# flag를 사용하여 reverse는 마지막 한 번만 실행하도록 한다.
import sys
from collections import deque
input = sys.stdin.readline

def getAnswer(dq, cmd, back):
  for i in cmd:
    if i == "R":
      back = (back+1)%2
    else:
      if len(dq) != 0:
        if back == 1:
          dq.pop()
        else:
          dq.popleft()
      else:
        print("error")
        break
  else:
    print("[", end="")
    if back == 1:
      print(",".join(list(dq)[::-1]), end="")
    else:
      print(",".join(list(dq)), end="")
    print("]")

t = int(input())

for _ in range(t):
  cmd = input().rstrip()
  n = int(input())
  lst = input().rstrip()
  if n == 0:
    dq = deque()
  else:
    dq = deque(list(lst[1:-1].split(",")))
  getAnswer(dq, cmd, 0)