import sys
from collections import deque
input = sys.stdin.readline

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
room = []
for _ in range(n):
    room.append(list(input()))

# 문 위치 구하기
door = []
for i in range(n):
    for j in range(n):
        if room[i][j] == '#':
            door.append((i, j))

visited = [[[-1] * 4 for _ in range(n)] for _ in range(n)]
dq = deque()
sx, sy = door[0]
# 상화좌우 모두 초기값으로 설정
for i in range(4):
    visited[sx][sy][i] += 1
    dq.append((i, sx, sy))

while dq:
    dir, curx, cury = dq.popleft()

    # bfs로 최소 거울 수 찾기 완료!
    if door[1] == (curx, cury):
        print(visited[curx][cury][dir])
        break

    nx = curx + dx[dir]
    ny = cury + dy[dir]
    if 0<=nx<n and 0<=ny<n and room[nx][ny] != '*':
        if visited[nx][ny][dir] == -1 or visited[nx][ny][dir] > visited[curx][cury][dir]:
            visited[nx][ny][dir] = visited[curx][cury][dir]
            dq.appendleft((dir, nx, ny))
        
    if room[curx][cury] == '!':
        ndirs = (2, 3) if dir in (0, 1) else (0, 1)
        for ndir in ndirs:
            nx = curx + dx[ndir]
            ny = cury + dy[ndir]

            if 0<=nx<n and 0<=ny<n and room[nx][ny] != '*':
                if visited[nx][ny][ndir] == -1 or visited[nx][ny][ndir] > visited[curx][cury][dir] + 1:
                    visited[nx][ny][ndir] = visited[curx][cury][dir] + 1
                    dq.append((ndir, nx, ny))