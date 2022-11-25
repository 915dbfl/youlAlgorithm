# #22.11.25
# #정수 삼각형
# #class4/실버 1
# dp

# bfs: 시간초과
import sys

def dfs(y, x, sum):
  global ans
  if y == n-1:
    ans = max(ans, sum)
    return

  dfs(y+1, x, sum+triangle[y+1][x])
  dfs(y+1, x+1, sum+triangle[y+1][x+1])


n = int(sys.stdin.readline())
triangle = []

for _ in range(n):
  triangle.append(list(map(int, sys.stdin.readline().split())))
  
ans = 0
dfs(0, 0, triangle[0][0])
print(ans)

# dp
import sys

n = int(sys.stdin.readline())
triangle = []

for _ in range(n):
  triangle.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
  for j in range(i+1):
    if j == 0:
      triangle[i][0] += triangle[i-1][0]
    elif j == i:
      triangle[i][j] += triangle[i-1][j-1]
    else:
      triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

print(max(triangle[n-1]))