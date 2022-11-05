#22.11.05
#2*n 타일링
#class3/실버3
#dp

lst = [1, 2, 3]

n = int(input())

for _ in range(2, n):
  lst.append(lst[-1]+lst[-2])

print(lst[n-1]%10007)