#22.09.24
#스택수열
#class2_1
#stack

import sys

N = int(sys.stdin.readline())
sequence = []
stack = [0]
answer = []
target = 1
index = 0

for i in range(N):
  sequence.append(int(sys.stdin.readline()))

while index < N:
  a = stack[-1]
  b = sequence[index]
  if a == b:
    answer.append("-")
    stack.pop()
    index += 1
  elif a < b:
    answer.append("+")
    stack.append(target)
    target += 1
  else:
    print("NO")
    break
else:
  for i in answer:
    print(i)

# sequence[0]을 계속해서 pop하는 방식으로 진행했는데 시간이 많이 걸렸다.
# pop(0)는 0번쨰의 인덱스를 뺴며 1-(n-1)요소들이 한 칸씩 앞 당겨지는 shift 연산이 일어나게 된다.
# 즉, list에서의 pop(i) 연산은 O(N)의 시간복잡도를 갖는다.