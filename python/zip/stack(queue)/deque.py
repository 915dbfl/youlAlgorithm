#22.10.05
#덱
#class2/실버4
#deque

import sys
from collections import deque

class Deque:
  def __init__(self):
    self.deque = deque()

  def push_front_X(self, num):
    self.deque.appendleft(num)

  def push_back_X(self, num):
    self.deque.append(num)

  def empty(self):
    if self.size() == 0:
      return 1
    else:
      return 0

  def pop_back(self):
    if self.empty() == 1:
      return -1
    else:
      return self.deque.pop()

  def pop_front(self):
    if self.empty() == 1:
      return -1
    else:
      return self.deque.popleft()

  def size(self):
    return len(self.deque)
  
  def front(self):
    if self.empty() == 1:
      return -1
    else:
      return self.deque[0]

  def back(self):
    if self.empty() == 1:
      return -1
    else:
      return self.deque[-1]
    

n = int(sys.stdin.readline())
dq = Deque()

for i in range(n):
  cmd = sys.stdin.readline().rstrip()
  
  if "push" in cmd:
    cmd, num = cmd.split()

  if cmd == "push_back":
    dq.push_back_X(int(num))
  elif cmd == "push_front":
    dq.push_front_X(int(num))
  elif cmd == "pop_back":
    print(dq.pop_back())
  elif cmd == "pop_front":
    print(dq.pop_front())
  elif cmd == "size":
    print(dq.size())
  elif cmd == "empty":
    print(dq.empty())
  elif cmd == "front":
    print(dq.front())
  else:
    print(dq.back())