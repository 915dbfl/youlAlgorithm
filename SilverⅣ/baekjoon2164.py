#21.09.23
N = int(input())
if N == 1:
  print(1)
else:
 num = 1
 while num < N:
    num *= 2
 print((N - (num // 2)) * 2)