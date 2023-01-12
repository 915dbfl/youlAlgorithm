#23.01.12
#N-Queen
#골드 4

#백트래킹
n = int(input())

def check(i, j):
  for d in range(1, i+1):
    if j-d >= 0 and visited[j-d] == i-d:
      return False
    if j+d < n and visited[j+d] == i-d:
      return False
  return True

def setQueen(i):
  global answer
  if i == n:
    answer += 1
    return

  for j in range(n):
    if visited[j] == -1 and check(i, j):
      visited[j] = i
      setQueen(i+1)
      visited[j] = -1

answer = 0
visited = [-1 for _ in range(n)]

setQueen(0)

print(answer)
