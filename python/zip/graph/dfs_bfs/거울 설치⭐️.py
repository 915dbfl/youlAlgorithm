import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# 시작하는 문의 x, y
ox, oy = -1, -1
# 끝나는 문의 x, y
cx, cy = -1, 1

for i in range(n):
    for j in range(n):
        if arr[i][j] == "#":
            if ox == -1 and oy == -1:
                ox, oy = i, j
            else:
                cx, cy = i, j

check = [[[-1] * 4 for _ in range(n)] for _ in range(n)]
q = deque()

# 시작 지점에서 시작 방향 설정
for i in range(4):
    q.append((ox, oy, i))
    check[ox][oy][i] = 0

while q:
    x, y, dir = q.popleft()
    # 현재 지점이 닫는 문이면 정답 출력 후 바로 종료
    if x == cx and y == cy:
        print(check[x][y][dir])
        break

    nx, ny = x + dx[dir], y + dy[dir]
    # 범위에 만족하는 경우
    if 0 <= nx < n and 0 <= ny < n:
        # 벽이 아닌 경우
        if arr[nx][ny] != "*":
            # 처음 방문한 곳 / 더 적은 횟수로 갈 수 있는 곳
            # 큐의 가장 앞에 삽입
            if check[nx][ny][dir] == -1 or check[nx][ny][dir] > check[x][y][dir]:
                check[nx][ny][dir] = check[x][y][dir]
                q.appendleft((nx, ny, dir))

            # 거울을 놓는 경우
            # 거울 설치 -> 큐의 뒷부분에 삽입
            if arr[nx][ny] == "!":
                # 북, 남 -> 동, 서로 반사
                # 동, 서 -> 북, 남으로 반사
                nds = [2, 3] if dir < 2 else [0, 1]
                for nd in nds:
                    if check[nx][ny][nd] == -1 or check[nx][ny][nd] > check[x][y][dir] + 1:
                        check[nx][ny][nd] = check[x][y][dir] + 1
                        q.append((nx, ny, nd))