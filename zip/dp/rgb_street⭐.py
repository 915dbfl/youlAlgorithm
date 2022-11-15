#22.11.14
#rgb거리
#class4/실버1
#dp

#dfs: 시간초과(3^1000)
import sys

def dfs(pri, cur, cost):
  global answer
  if cur == n:
    answer = min(answer, cost)
    return
  
  if cost >= answer:
    return
  
  if pri == 0:
    dfs(2, cur+1, cost+rgbs[cur][2])
    dfs(1, cur+1, cost+rgbs[cur][1])
  elif pri == 1:
    dfs(2, cur+1, cost+rgbs[cur][2])
    dfs(0, cur+1, cost+rgbs[cur][0])
  else:
    dfs(1, cur+1, cost+rgbs[cur][1])
    dfs(0, cur+1, cost+rgbs[cur][0])

n = int(sys.stdin.readline())

answer = 1000*n
rgbs = []
for _ in range(n):
  rgbs.append(list(map(int, sys.stdin.readline().split())))

dfs(0, 1, rgbs[0][0])
dfs(1, 1, rgbs[0][1])
dfs(2, 1, rgbs[0][2])
print(answer)

#dp
import sys

n = int(sys.stdin.readline())

rgbs = []

for _ in range(n):
  rgbs.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
  rgbs[i][0] = min(rgbs[i-1][1], rgbs[i-1][2])+rgbs[i][0]
  rgbs[i][1] = min(rgbs[i-1][0], rgbs[i-1][2])+rgbs[i][1]
  rgbs[i][2] = min(rgbs[i-1][0], rgbs[i-1][1])+rgbs[i][2]

print(min(rgbs[-1]))

# # dp 토글링
import sys

n = int(sys.stdin.readline())

rgb = list(map(int, sys.stdin.readline().split()))

for _ in range(n-1):
  r, g, b = map(int, sys.stdin.readline().split())
  r = min(rgb[1], rgb[2])+r
  g = min(rgb[0], rgb[2])+g
  b = min(rgb[0], rgb[1])+b

  rgb = [r, g, b]

print(min(rgb))