# 21.08.06
import sys
num = int(input())
name1 = list(input())
for i in range(num-1):
  name2 = list(input())
  for j in range(len(name1)):
    if name1[j] != name2[j]:
      name1[j] = '?'
print(''.join(name1))