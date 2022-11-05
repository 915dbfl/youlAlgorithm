#22.11.05
#2*n 타일링2
#class3/실버3
#dp

lst = [0, 1, 3, 5]

n = int(input())

for i in range(4, n+1):
  if i%2 == 0:
    lst.append(lst[-1]*2+1)
  else:
    lst.append(lst[-1]*2-1)

print(lst[n]%10007)