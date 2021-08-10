#21.08.10
num = int(input())
for _ in range(num):
  line = input()
  for i in range(len(line) - 1):
    if line.find(line[i]) > line.find(line[i + 1]):
      num -= 1
      break
print(num)