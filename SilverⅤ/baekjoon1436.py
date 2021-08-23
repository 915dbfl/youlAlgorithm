#21.08.23
num = int(input())
result = 0
fnt = count = 0
lst = [600, 660, 666]

while num != count:
  if len(str(fnt)) >= 3 and str(fnt).count("666") != 0:
    result = fnt*1000
    count += 1
    while count != num:
      result += 1
      count += 1
      if result % 1000 == 999:
        break
    fnt += 1
  elif fnt % 100 == 66:
    result = int(str(fnt) + str(lst[0]))
    lst[0] += 1
    count += 1
    if lst[0] == 700:
      fnt += 1
      lst[0] = 600 
  elif fnt % 10 == 6:
    result = int(str(fnt) + str(lst[1]))
    lst[1] += 1
    count += 1
    if lst[1] == 670:
      fnt += 1
      lst[1] = 660
  else:
    result = int(str(fnt) + str(lst[2]))
    count += 1
    fnt += 1
print(result)