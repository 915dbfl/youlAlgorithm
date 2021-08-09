#21.08.09
lst = list(input())
for i in range(len(lst)):
  # 소문자의 경우
  if lst[i].islower(): 
    lst[i] = chr((ord(lst[i])-97 + 13)%26 + 97)
  # 대문자의 경우
  elif lst[i].isupper():
    lst[i] = chr((ord(lst[i])-65 + 13)%26 + 65)
print(''.join(lst))