#21.08.12
cro_lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
for i in cro_lst:
  if i in word:
    word = word.replace(i, " ")
print(len(word))