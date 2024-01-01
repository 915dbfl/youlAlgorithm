#21.08.25
x = int(input())
lst = [64]
while True:
  if sum(lst) == x:
    break
  else:
    m = lst.pop()
    temp = m //2
    if x > sum(lst) + temp:
      lst.append(temp)
    lst.append(temp)
print(len(lst))