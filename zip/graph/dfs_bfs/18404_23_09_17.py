# 현명한 나이트

# bfs
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
nx, ny = map(int, sys.stdin.readline().split())
enemy = []
move = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
visited = [[sys.maxsize]*(n+1) for _ in range(n+1)]

def bfs():
    global nx, ny
    dq = deque()
    dq.append((nx, ny))
    visited[nx][ny] = 0

    while dq:
        cx, cy = dq.popleft()

        for i in range(8):
            newX = cx + move[i][0]
            newY = cy + move[i][1]
            mv = visited[cx][cy]

            if 1 <= newX <= n and 1 <= newY <= n and visited[newX][newY] > mv + 1:
                visited[newX][newY] = mv + 1
                dq.append((newX, newY))

bfs()
answer = []
for _ in range(m):
    ex, ey = map(int, sys.stdin.readline().split())
    answer.append(str(visited[ex][ey]))

print(" ".join(answer))
