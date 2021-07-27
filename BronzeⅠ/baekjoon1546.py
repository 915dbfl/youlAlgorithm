#21.07.27
num = int(input())
lst = list(map(int, input().split()))
max = max(lst)
for i in range(num):
  lst[i] = lst[i] / max * 100
print(sum(lst) / num)

