#21.12.30
#유기농 배추
import sys
test = int(sys.stdin.readline().rstrip())
for k in range(test):
  w, h, c = map(int,sys.stdin.readline().rstrip().split())
  lst = []
  checkLst = []
  count = 0
  for l in range(c):
    lst.append(list(map(int, sys.stdin.readline().rstrip().split())))

  lst.sort(key= lambda x: (x[0], x[1]))

  for i in lst:
    checkValue = 0
    check = 0
    if len(checkLst) == 0:
      count += 1
      checkLst.append(i)
    else:
      for j in checkLst:
        if i[0] == j[0]:
          if i[1]-1 == j[1]:
            checkValue += 1
        elif i[1] == j[1]:
          if i[0]-1 == j[0]:
            checkValue += 1
        elif i[0]-1 == j[0] and i[1]-1 == j[1]:
          check = 1
      checkLst.append(i)
      if checkValue == 0:
        count += 1
      elif checkValue == 2:
        if check == 0:
          count -= 1

  print(count)