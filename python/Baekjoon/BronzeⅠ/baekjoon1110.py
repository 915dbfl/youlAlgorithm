#21.07.27
num = int(input())
new_num = num
count = 0
while(count == 0 or new_num != num):
  count += 1
  sum = new_num // 10 + new_num % 10
  new_num = (new_num % 10) * 10  + sum % 10
print(count)