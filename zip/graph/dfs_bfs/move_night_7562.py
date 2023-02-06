#23.02.06
#나이트의 이동
#실버1
#알고리즘 6주차 - bfs

import sys
from collections import deque

def bfs():
    graph = [[0]*size for _ in range(size)]
    q = deque([[0, start[0], start[1]]])
    graph[start[0]][start[1]] = 1

    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]

    while q:
        c, x, y = q.popleft()

        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<size and 0<=ny<size and graph[nx][ny] == 0:
                if nx == end[0] and ny == end[1]:
                    print(c+1)
                    return
                else:
                    graph[nx][ny] = 1
                    q.append([c+1, nx, ny])

t = int(sys.stdin.readline())

for _ in range(t):
    size = int(sys.stdin.readline())

    start = list(map(int, sys.stdin.readline().split()))
    end = list(map(int, sys.stdin.readline().split()))

    if start == end:
        print(0)
    else:
        bfs()