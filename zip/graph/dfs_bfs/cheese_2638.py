#23.03.06
#치즈
#골드3
#bfs, dfs

#bfs
import sys
from collections import deque
input = sys.stdin.readline

def contactAir(): # 공기가 맞닿는 가장자리 부분만 치즈에 영향을 준다.
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<m:
                if paper[nx][ny] == 1:
                    visited[nx][ny] += 1
                else:
                    if visited[nx][ny] == 0:
                        q.append((nx, ny))
                        visited[nx][ny] = 1

def getMelted():
    result = False # 녹는 치즈가 있는지 check

    for i in range(n):
        for j in range(m):
            if paper[i][j] == 1 and visited[i][j] >= 2: # 공기가 닿는 부분이 2 이상인지 확인
                result = True
                paper[i][j] = 0

    return result

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

time = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

while 1:
    visited = [[0]*m for _ in range(n)]

    # 시간이 1씩 증가할 때마다 공기에 닿아 치즈가 녹는 과정이 반복된다.
    contactAir()

    if getMelted(): # 녹는 치즈가 있을 경우
        time += 1 # 시간이 1 증가하고
    else: # 없을 경우
        print(time) # 모든 치즈가 높은 것이므로 출력!
        exit()