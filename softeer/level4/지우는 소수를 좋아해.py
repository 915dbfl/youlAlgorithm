# dfs
import sys
from collections import defaultdict, deque

INF = sys.maxsize
n, m = map(int, sys.stdin.readline().split())
graph = defaultdict(list)

for _ in range(m):
  a, b, c = map(int, sys.stdin.readline().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

dq = deque([(1, 0)])
min_visited = [INF] * (n+1)
min_visited[1] = 0
result = sys.maxsize
while dq:
  cur, Min = dq.popleft()

  if cur == n and result > Min: #최종 레벨이 더 작은 걸 선택
    result = Min
    continue

  for nxt, level in graph[cur]: #해당 위치에서 갈 수 있는 모든 경우 확인
    if min_visited[nxt] > max(level, Min): #해당 위치에 갈 수 있는 최소 레벨
      min_visited[nxt] = max(level, Min)
      dq.append((nxt, max(level, Min)))

result += 1
while 1:
  for i in range(2, int(result**0.5)+1):
    if result % i == 0:
      result += 1
      break
  else:
    print(result)
    break