#23.01.20
#숨바꼭질2
#골드4

#bfs
import sys
from collections import deque

def bfs(str):
  global min_sec, answer
  dq = deque([[str, 0]])
  visited = set([str]) # visited을 체크해 한 번 방문한 곳 재방문하지 않음

  while dq:
    cur, sec = dq.popleft()
    visited.add(cur)

    if sec > min_sec:
      return

    if cur == k:
      min_sec = sec
      answer += 1
    else:
      for i in [cur-1, cur+1, cur*2]:
        if 0 <= i <= 100000 and i not in visited:
          dq.append([i, sec+1])

n, k = map(int, sys.stdin.readline().split())
answer = 0
min_sec = abs(n-k)

bfs(n)
print(min_sec)
print(answer)

#리팩토링
import sys
from collections import deque

def bfs(n):
  dq = deque([n])
  visited[n][0] = 0 # n까지 걸리는 시간은 0
  visited[n][1] = 1 # 자기 자신이므로 방법은 1

  while dq:
    x = dq.popleft()

    for i in [x-1, x+1, x*2]:
      if 0<=i<=100000:
        if visited[i][0] == -1: # 첫 방문일 경우
          visited[i][0] = visited[x][0]+1 # bfs이므로 해당 시간이 최단 시간
          visited[i][1] = visited[x][1]
          dq.append(i)

        elif visited[i][0] == visited[x][0]+1: # 이미 방문했고, 최단 시간인 경우
          visited[i][1] += visited[x][1]

n, k = map(int, sys.stdin.readline().split())
visited = [[-1, 0] for _ in range(100001)]

bfs(n)
print(visited[k][0])
print(visited[k][1])