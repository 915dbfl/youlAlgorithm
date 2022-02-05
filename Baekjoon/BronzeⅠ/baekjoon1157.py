#21.07.30
str = input().upper()
cnt_lst = []
for i in set(str):
  cnt_lst.append(str.count(i))
if cnt_lst.count(max(cnt_lst)) > 1:
  print('?')
else:
  print(list(set(str))[cnt_lst.index(max(cnt_lst))])