#22.02.03
#2644: 촌수계산

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(num, chk):
  global lst, a, b
  for j in lst[num-1]:
    if j == b:
      print(chk+1)
      check[0] = True
      return
    elif check[j] == False:
      check[j] = True
      dfs(j, chk+1)


n = int(input())
a, b = map(int, input().split())
m = int(input())
lst = [[] for _ in range(n)]

for _ in range(m):
  x, y = map(int, input().split())
  lst[x-1].append(y)
  lst[y-1].append(x)

check = [False for _ in range(n+1)]
check[a] = True
dfs(a, 0)
if check[0] == False:
  print(-1)

