# 21.08.10
def d(n):
  lst = list(map(int, str(n)))
  return n + sum(lst)

d_num = set()
for i in range(1, 10001):
  d_num.add(d(i))

for i in range(1, 10001):
  if i in d_num:
    pass
  else:
    print(i)