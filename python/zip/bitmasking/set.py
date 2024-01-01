#22.11.11
#집합
#class3/실버5
#비트마스킹

import sys

n = int(sys.stdin.readline())
s = set()

for _ in range(n):
  cmd = sys.stdin.readline().rstrip()
  if cmd == "all":
    s = set([i for i in range(1, 21)])
  elif cmd == "empty":
    s.clear()
  else:
    op, val = cmd.split()
    val = int(val)

    if op == "add":
      s.add(val)
    elif op == "remove" and val in s:
      s.remove(val)
    elif op == "check":
      print(1 if val in s else 0)
    elif op == "toggle":
      if val in s:
        s.remove(val)
      else:
        s.add(val)

# remove 대신 discard를 사용해 없는 수일 경우에도 오류가 나지 않게 한다.
import sys

n = int(sys.stdin.readline())
s = set()

for _ in range(n):
  cmd = sys.stdin.readline().rstrip()
  if cmd == "all":
    s = set([i for i in range(1, 21)])
  elif cmd == "empty":
    s.clear()
  else:
    op, val = cmd.split()
    val = int(val)

    if op == "add":
      s.add(val)
    elif op == "remove":
      s.discard(val)
    elif op == "check":
      print(1 if val in s else 0)
    elif op == "toggle":
      if val in s:
        s.discard(val)
      else:
        s.add(val)

# 비트마스킹
import sys

s = 0
n = int(input())
answer = 0

for _ in range(n):
  command = sys.stdin.readline().rstrip()

  if command == "all":
    answer = (1<<20)-1
  elif command == "empty":
    answer = 0
  else:
    op, val = command.split()
    val = int(val)-1
    if op == "add":
      answer |= (1<<val)
    elif op == "remove":
      answer &= ~(1<<val)
    elif op == "check":
      if answer & (1<<val) != 0:
        print(1)
      else:
        print(0)
    else:
      answer ^= (1<<val)