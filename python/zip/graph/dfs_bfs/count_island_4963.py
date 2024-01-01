#23.02.06
#섬의 개수
#실버 2
#알고리즘 6주차 - bfs

import sys
sys.setrecursionlimit(10**4)

def dfs(x, y):
    graph[x][y] = 2

    dx = [1, 1, 1, 0, -1, -1, -1, 0]
    dy = [1, 0, -1, -1, -1, 0, 1, 1]

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<h and 0 <=ny<w and graph[nx][ny] == 1:
            dfs(nx, ny)

while 1:
    w, h = map(int, sys.stdin.readline().split())

    if w == 0 and h == 0:
        break
    else:
        graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
        count = 0

        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1:
                    count += 1
                    dfs(i, j)
        
        print(count)