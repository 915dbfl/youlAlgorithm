#21.01.08
#11724: 연결 요소의 개수
#bfs 사용하기

import sys
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(m):
  f, b = map(int, sys.stdin.readline().split())
  graph[f].append(b)
  graph[b].append(f)

def bfs(v):
  order = [v]
  while order:
    t = order.pop()
    for j in graph[t]:
      if visited[j] == 0:
        order.append(j)
        visited[j] = 1

result = 0
for k in range(1, n+1):
  if visited[k] == 0:
    bfs(k)
    result += 1

print(result)
