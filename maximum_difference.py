#22.10.23
#차이를 최대로
#class3/실버2

#오답
from collections import deque

n = int(input())
lst = list(map(int, input().rstrip().split()))

dq = deque(sorted(lst))
a = dq.popleft()
b = a
r = 0
answer = 0

while dq:
  if r % 2 != 0:
    tmp = dq.popleft()
  else:
    tmp = dq.pop()
  
  if abs(a-tmp) > abs(b-tmp):
    answer += abs(a-tmp)
    a = tmp
  else:
    answer += abs(b-tmp)
    b = tmp
  r += 1

print(answer)