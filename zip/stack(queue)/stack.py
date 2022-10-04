#22.10.04
#스택
#class2/실버4
#stack/queue

import sys

class Stack:
  def __init__(self):
    self.stack = []

  def push(self, num):
    self.stack.append(num)

  def empty(self):
    if len(self.stack) == 0:
      return 1
    else:
      return 0

  def pop(self):
    if self.empty() == 1:
      return -1
    else:
      return self.stack.pop()
  
  def size(self):
    return len(self.stack)
  
  def top(self):
    if self.empty() == 1:
      return -1
    else:
      return self.stack[-1]
    

n = int(sys.stdin.readline())
stack = Stack()

for i in range(n):
  cmd = sys.stdin.readline().rstrip()
  
  if "push" in cmd:
    cmd, num = cmd.split()

  if cmd == "push":
    stack.push(int(num))
  elif cmd == "pop":
    print(stack.pop())
  elif cmd == "size":
    print(stack.size())
  elif cmd == "empty":
    print(stack.empty())
  elif cmd == "top":
    print(stack.top())