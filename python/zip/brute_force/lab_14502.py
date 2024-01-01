#23.01.27
#연구소
#골드4
#브루트포스, 너비 우선 탐색

#브루트포스를 벽 세 개를 세울 수 있는 모든 경우의 수 확인
#각 경우마다 bfs를 통해 안전영역 수 세기

import sys
from collections import deque
from copy import deepcopy
from itertools import combinations

def countVirus(walls):
  tmp = deepcopy(graph) #깊은 복사

  for x, y in walls: #벽 추가
    tmp[x][y] = 1

  visited = [[0]*m for _ in range(n)] #방문 리스트

  dx = [0, -1, 0, 1]
  dy = [-1, 0, 1, 0]

  que = deque(virus_zone)

  for x, y in virus_zone:
    visited[x][y] = 1

  while que:
    x, y = que.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<= nx < n and 0<= ny < m and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        if tmp[nx][ny] == 0:
          tmp[nx][ny] = 2
          que.append([nx, ny])

  tmp_ans = 0
  for c in tmp: #바이러스 x 영역 카운트
    tmp_ans += c.count(0)

  return tmp_ans

def setWall():
  global answer
  for c in combinations(clean_zone, 3):
    answer = max(answer, countVirus(c))

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 0
virus_zone = []
clean_zone = []

for i in range(n): #virus의 수와 빈 공간 파악
  for j in range(m):
    if graph[i][j] == 2:
      virus_zone.append([i, j])
    elif graph[i][j] == 0:
      clean_zone.append([i, j])

setWall()
print(answer)