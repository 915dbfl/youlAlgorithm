#21.07.25
test = int(input())
for i in range(test):
  num, case = input().split()
  for i in case:
    print(i * int(num), end= "")
  print()