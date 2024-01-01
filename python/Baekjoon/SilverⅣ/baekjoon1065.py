#21.08.27
n = input()
if len(n) < 3:
  print(int(n))
else:
  count = 99
  for i in range(100, int(n)+1):
    lst = [int(k) for k in str(i)]
    if lst[1] - lst[0] == lst[2] - lst[1]:
      count += 1
  print(count)
