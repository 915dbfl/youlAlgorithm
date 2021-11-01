#21.11.01
import sys
N, M, V = map(int, input().split())
lst = []
lst1 = []
lst2 = []
order_bfs = [V]
key_index = 0
for i in range(M):
  lst.append(list(map(int, sys.stdin.readline().split())))

lst.sort(key= lambda i : (i[0], i[1]))
for i in lst:
  lst1.append(i[0])
  lst2.append(i[1])

while len(lst1) > 0:
  V = order_bfs[key_index]
  if V in lst1:
    idx = lst1.index(V)
    if lst2[idx] not in order_bfs:
      order_bfs.append(lst2[idx])
    lst1.pop(idx)
    lst2.pop(idx)
  elif V in lst2:
    idx = lst2.index(V)
    if lst1[idx] not in order_bfs:
      order_bfs.append(lst1[idx])
    lst1.pop(idx)
    lst2.pop(idx)
  else:
    key_index += 1



print(order_bfs)
  

