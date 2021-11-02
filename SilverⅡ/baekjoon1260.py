#21.11.01
#시간초과
import sys
N, M, V = map(int, sys.stdin.readline().split())
order_bfs = [V]
order_dfs = [V]
key = 0
dic = {}
for i in range(M):
  temp1, temp2 = map(int, sys.stdin.readline().split())
  if temp1 not in dic.keys():
    dic[temp1] = []
  if temp2 not in dic.keys():
    dic[temp2] = []
  dic[temp1].append(temp2)
  dic[temp2].append(temp1)

for i in dic.keys():
  dic[i].sort()

print(V, end=" ")
while len(order_bfs) < len(dic.keys()):
  for i in dic[V]:
    if i not in order_bfs:
      order_bfs.append(i)
      print(i, end = " ")
  key += 1
  V = order_bfs[key]

print("")
print(order_dfs[0], end=" ")
V = order_dfs[0]

while len(order_dfs) < len(dic.keys()):
  for i in dic[V]:
    if i not in order_dfs:
      order_dfs.append(i)
      print(i, end=" ")
      V = i
      break