#21.10.26
n= int(input())
lst = [0, 1, 3]
for i in range(3, n+1):
  temp = 3*lst[i-2] + (lst[i-1] - lst[i-2])
  lst.append(temp)
print(lst[n]%10007)