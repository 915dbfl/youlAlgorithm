#22.11.14
#rgb거리
#class4/실버1
#dfs

#dfs: 시간초과
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
