# 메모리 초과 및 시간 초과

import sys
from collections import deque
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
graph = []
tmp_graph = [[0] * m for _ in range(n)]
answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

def checkSafeArea(): # 바이러스 퍼뜨리기 + 안전 구역 확인
    # 바이러스를 퍼뜨리고 안전 구역을 확인할 graph 새로 생성
    tmp_graph = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            tmp_graph[i][j] = graph[i][j]

    # 바이러스 퍼뜨리기
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                dq = deque([[i, j]])

                while dq:
                    cx, cy = dq.popleft()

                    for k in range(4):
                        nx = cx + dx[k]
                        ny = cy + dy[k]

                        if 0 <= nx < n and 0 <= ny < m and tmp_graph[nx][ny] == 0:
                            tmp_graph[nx][ny] = 2 # 바이러스 퍼뜨리기
                            dq.append([nx, ny])

    # 안전 구역 확인
    safeArea = 0
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 0:
                safeArea += 1
    return safeArea

def setWall(wcnt):
    global answer
    if wcnt == 3: # 모든 벽을 다 세웠을 경우
        result = checkSafeArea()
        answer = max(answer, result)
    else:
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    setWall(wcnt+1)
                    graph[i][j] = 0

setWall(0)
print(answer)

# 모범 답안
n, m = map(int, input().split())
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# dfs를 활용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 상하좌우 중에서 바이러스가 퍼질 수 있는 경우
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                    temp[nx][ny] = 2
                    virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# dfs를 활용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최대값 계산
        result = max(result, get_score())
        return
    # 빈 공간에 울타리를 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)

# combination 활용
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