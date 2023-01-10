#22.10.22
#AC
#class3/골드5
#queue

# 'R'에서 revrse를 할 경우, 시간초과가 발생! -> O(N)
# flag를 사용하여 reverse는 마지막 한 번만 실행하도록 한다.
#시간초과
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  funcs = input().rstrip()

  n = int(input())
  if n == 0:
    dq = deque(input().rstrip()[1:1])
  else:
    dq = deque(input().rstrip()[1:n*2].split(","))

  for c in funcs:
    if c == "D":
      if len(dq) > 0:
        dq.popleft()
      else:
        print("error")
        break
    else:
      dq = deque(list(dq)[::-1])
  else:
    print("[")
    print(",".join(dq), end = "")
    print("]")

# 리팩토링
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  funcs = input().rstrip()
  check_d = 0

  n = int(input())
  if n == 0:
    dq = deque(input().rstrip()[1:-1])
  else:
    dq = deque(input().rstrip()[1:-1].split(","))

  for c in funcs:
    if c == "D":
      if len(dq) > 0:
        if check_d:
          dq.pop()
        else:
          dq.popleft()
      else:
        print("error")
        break
    else:
      check_d = abs(check_d-1)
  else:
    if check_d:
      dq = list(dq)[::-1]

    print("[", end= "")
    print(",".join(dq), end = "")
    print("]")