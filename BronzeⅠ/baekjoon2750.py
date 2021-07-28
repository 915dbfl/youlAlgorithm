# #21.07.28
num = int(input())
lst = []
for i in range(num):
  lst.append(int(input()))
for i in sorted(lst, reverse= False):
  print(i)