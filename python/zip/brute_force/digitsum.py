#22.09.26
#분해합
#class2/브론즈2
#brute_force

N = input()

for i in range(int(N)-9*len(N), int(N)-(1*len(N))+1):
  s = sum(map(int, str(abs(i)))) + i
  if str(s) == N:
    print(i)
    break
else:
  print(0)