# 21.09.20
num = int(input())
if num == 1:
  print("")
else:
  lst_check = 0
  while num != 1 and lst_check == 0:
    if num == 3 or num == 2:
      print(num)
      break
    else:
      for i in range(2, int(num ** 0.5)+1, 1):
        if num % i == 0:
          print(i)
          num = num // i
          break
        if i == int(num**0.5):
          lst_check = 1
          print(num)
          break