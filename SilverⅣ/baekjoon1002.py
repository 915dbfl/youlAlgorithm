#21.09.05
n = int(input())
for i in range(n):
  test = list(map(int, input().split()))
  if test[0] == test[3] and test[1] == test[4]:
    if test[2] == test[5]:
      print(-1)
    else:
      print(0)
  else:
    r1 = ((test[3] - test[0])**2 + (test[4] - test[1])**2)**0.5
    r2 = test[2] + test[5]
    if r1 < r2:
      lst = [test[2], test[5]]
      lst.sort()
      if r1 + lst[0] == lst[1]:
        print(1)
      elif r1 + lst[0] < lst[1]:
        print(0)
      elif r1 + lst[0] > lst[1]:
        print(2)
    elif r1 == r2:
      print(1)
    elif r1 > r2:
      print(0)