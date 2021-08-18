#21.08.18
m = int(input())
n = int(input())
prime = []
for i in range(m, n+1):
  if i != 1:
    check = 1
    for j in range(2, int(i**0.5)+1):
      if i % j == 0 :
        check = 0
        break
    if check:
      prime.append(i)
if len(prime) == 0:
  print(-1)
else:
  print(sum(prime))
  print(prime[0])