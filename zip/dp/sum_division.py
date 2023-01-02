#23.01.02
#합분해
#알고리즘 스터디 2주차 -3

#dfs 시간초과
import sys
input = sys.stdin.readline

def dfs(num, t):
  global answer
  if num == n:
    answer += 1
    return
  
  if t >= k:
    return
  
  for i in range(n+1):
    if num + i <= n:
      dfs(num+i, t+1)
      
answer = 0
n, k = map(int, input().split())

if n == k:
  print(1)
else:
  dfs(0, 0)
  print(answer%1000000000)

# dp 적용
import sys
input = sys.stdin.readline

answer = 0
n, k = map(int, input().split())

lst = [[1]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(2, k+1):
    lst[i][j] = lst[i][j-1] + lst[i-1][j]

print(lst[-1][-1]%1000000000)