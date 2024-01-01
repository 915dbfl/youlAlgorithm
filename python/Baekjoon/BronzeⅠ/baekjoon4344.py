#21.07.27
test = int(input())
for i in range(test):
  lst = list(map(int, input().split()))
  avg = sum(lst[1:]) / lst[0]
  count = 0
  for i in lst[1:]:
    if i > avg:
      count += 1
  print("%.3f%%" %((count/lst[0])*100))