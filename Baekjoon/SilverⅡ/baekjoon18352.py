#21.11.03
#BFS 사용
import sys
from collections import deque
# X로 시작해서 각 지점까지 갈 수 있는 최단 거리

N, M, K, X = map(int, sys.stdin.readline().split())
lst = [M+1 for _ in range(N+1)]
lst[X] = 0

#단방향 도로 저장 딕셔너리
road = [[] for _ in range(N+1)]
for j in range(M):
  temp1, temp2 = map(int, sys.stdin.readline().split())
  road[temp1].append(temp2)

que = deque([X])
while que:
  check = que.popleft()
  for j in road[check]:
    if lst[j] == M+1:
      que.append(j)
      lst[j] = lst[check] + 1

if K in lst:
  for i in range(1, N+1):
    if lst[i] == K:
      print(i)
else:
  print(-1)