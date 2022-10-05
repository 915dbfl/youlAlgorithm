#22.10.04
#요세푸스 문제 0
#class2/실버5
#queue, deque

n, k = map(int, input().split())

lst = list(range(1, n+1))
answer = []
cur = -1

while len(lst) > 0:
  cur = (cur + k) % len(lst)
  answer.append(str(lst.pop(cur)))
  cur -= 1

print("<", end= "")
print(", ".join(answer), end = "")
print(">")

#deque rotate 사용하기

from collections import deque

n, k = map(int, input().split())
dq = deque(range(1, n+1))

print("<", end = "")

for i in range(n):
  dq.rotate(-k)
  if i == n-1:
    print(dq.pop(), end = ">")
  else:
    print(dq.pop(), end = ", ")