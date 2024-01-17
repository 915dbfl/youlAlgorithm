# 어느 한 길이라도 inside에 도달하면 종료
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs():
    while dq:
        cx, cy = dq.pop()
        if cx + 1 == m:
            return "YES"
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0<=nx<m and 0<=ny<n and visited[nx][ny] == 0:
                if board[nx][ny] == "0":
                    visited[nx][ny] = 1
                    dq.append((nx, ny))

    return "NO"

m, n = map(int, input().split())
board = []
for _ in range(m):
    board.append(list(sys.stdin.readline().rstrip()))

dq = deque()
visited = [[0] * n for _ in range(m)]
for i in range(n):
    if board[0][i] == "0":
        visited[0][i] = 1
        dq.append((0, i))

print(dfs())