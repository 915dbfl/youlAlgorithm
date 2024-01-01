#22.10.17
#종이의 개수
#class3/실버2
#devide and conquer

from collections import defaultdict
import sys

def getNums(y, x, l):
  if l == 1:
    dic[graph[y][x]] += 1
  else:
    s = graph[y][x]
    for i in range(y, y+l):
      for j in range(x, x+l):
        if graph[i][j] != s:
          getNums(y, x, l//3)
          getNums(y+l//3, x, l//3)
          getNums(y+(l//3*2), x, l//3)
          getNums(y, x+l//3, l//3)
          getNums(y+l//3, x+l//3, l//3)
          getNums(y+(l//3*2), x+l//3, l//3)
          getNums(y, x+(l//3*2), l//3)
          getNums(y+l//3, x+(l//3*2), l//3)
          getNums(y+(l//3*2), x+(l//3*2), l//3)
          return
    else:
      dic[s] += 1

N = int(sys.stdin.readline())
graph = []
for _ in range(N):
  graph.append(list(map(int, sys.stdin.readline().split())))

dic = defaultdict(int)
getNums(0, 0, N)
print(dic[-1])
print(dic[0])
print(dic[1])