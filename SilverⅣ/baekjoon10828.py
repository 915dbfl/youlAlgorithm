#21.08.27
import sys
lst = []
n= int(sys.stdin.readline().rstrip())
for i in range(n):
  #split()을 통해 명령어 부분이 itr[0]에 들어있음
  itr = sys.stdin.readline().split()
  if itr[0] == "push":
    lst.append(itr[1])
  else:
    if itr[0] == "pop":
      if len(lst) == 0:
        sys.stdout.write("-1\n")
      else:
        sys.stdout.write(str(lst.pop()) + "\n")
    elif itr[0] == "size":
      sys.stdout.write(str(len(lst)) + "\n")
    elif itr[0] == "empty":
      if len(lst) == 0:
        sys.stdout.write("1\n")
      else:
        sys.stdout.write("0\n")
    elif itr[0] == "top":
      if len(lst) != 0:
        sys.stdout.write(str(lst[-1])+ "\n")
      else:
        sys.stdout.write("-1\n")