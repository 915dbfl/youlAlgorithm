#21.07.27
sugar = int(input())
count = 0
if sugar >= 3:
  for i in range(sugar // 5, -1, -1):
    if (sugar - 5 * i) % 3 == 0:
      count = i + (sugar - 5 * i) // 3
      break;
if count == 0:
  count = -1
print(count)