#22.09.25
#카드2
#class2_1
#deque

#기존 풀이
from collections import deque

N = int(input())
que = deque(range(1, N+1))

while len(que) > 1:
  que.popleft()
  que.append(que.popleft())

print(que[0])

#deque의 pop, append 시간복잡도는 O(1)

#리팩토링: 규칙을 이용한 풀이
N = int(input())

if N == 1 or N == 2:
  print(N)
else:
  n = 1
  while n < N:
    n *= 2

  print((N-(n//2))*2)