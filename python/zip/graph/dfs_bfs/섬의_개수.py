from collections import deque
import sys
input = sys.stdin.readline

def checkIsland(x, y, w, h):
    dq = deque()
    dq.append((x, y))
    graph[x][y] += 1

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    while dq:
        cx, cy = dq.popleft()

        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0<=nx<h and 0<=ny<w and graph[nx][ny] == 1:
                graph[nx][ny] += 1
                dq.append((nx, ny))
while 1:
    w, h = map(int, input().split())
    # 테스트 케이스 입력이 끝난 경우
    if w == 0 and h == 0:
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    islandCnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                checkIsland(i, j, w, h)
                islandCnt += 1

    print(islandCnt)