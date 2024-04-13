import sys
from collections import deque
input = sys.stdin.readline

# 상하좌우로 이동
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, board):
    dq = deque()
    dq.append([x, y])

    h = len(board)
    w = len(board[0])

    while dq:
        cx, cy = dq.popleft()

        if cx == h-1:
            return True

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0<=nx<h and 0<=ny<w and board[nx][ny] == 0:
                board[nx][ny] = 1
                dq.append([nx, ny])

    return False

m, n = map(int, input().split())
board = []

for i in range(m):
    board.append(list(map(int, list(input().rstrip()))))

for i in range(n):
    if board[0][i] == 0:
        flag = bfs(0, i, board)
        # 침투할 수 있다면
        if flag: 
            print("YES")
            break
else:
    print("NO")