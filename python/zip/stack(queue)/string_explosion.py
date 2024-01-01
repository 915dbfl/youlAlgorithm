#23.01.13
#문자열 폭발
#골드 4

#replace - 시간초과O(n^2)
#split, join - 시간초과O(n^2)
#stack 사용
import sys
input = sys.stdin.readline

str = input().rstrip()
exp_str = input().rstrip()
a = 0
l = len(exp_str)

answer = []
while a < len(str):
  answer.append(str[a])
  a += 1

  if len(answer) >= l:
    for i in range(1, l+1):
      if answer[-i] != exp_str[-i]:
        break
    else:
      for _ in range(l):
        answer.pop()

if answer:
  print(''.join(answer))
else:
  print('FRULA')

#리팩토링
import sys
input = sys.stdin.readline

str = input().rstrip()
exp_str = list(input().rstrip())
length = len(exp_str)

answer = []
for s in str:
  answer.append(s)

  if answer[-length:] == exp_str:
    answer[-length:] = []

if answer:
  print(''.join(answer))
else:
  print('FRULA')