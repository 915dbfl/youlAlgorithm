#21.10.26
n = int(input())
lst = [0, 1, 1, 2]
for i in range(4, n+1):
  lst.append(lst[i-1] + lst[i-2])
print(lst[n])