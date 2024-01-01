#22.10.03
#균형잡힌 세상
#class2/실버4
#queue

import sys

while 1:
  s = sys.stdin.readline().rstrip()
  brackets = []

  if s == ".":
    break
  
  for i in s:
    if i == ")":
      if (brackets[-1:] != [] and brackets[-1] != "(") or brackets[-1:] == []:
        print("no")
        break
      else:
        brackets.pop()
    elif i == "]":
      if (brackets[-1:] != [] and brackets[-1] != "[") or brackets[-1:] == []:
        print("no")
        break
      else:
        brackets.pop()
    elif i == "(" or i == "[":
      brackets.append(i)
  else:
    print("yes" if len(brackets) == 0 else "no")

