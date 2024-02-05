import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    dq = deque([(0, 0)])
    visited = [[0] * c for _ in range(r)]
    visited[0][0] = 1
    existC = False
    cheese = 0

    while dq:
        x, y = dq.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == 0: # 범위 내에 있고, 방문하지 않았을 경우
                visited[nx][ny] = 1
                if board[nx][ny] == 1: # 치즈일 경우
                    cheese += 1
                    existC = True
                    board[nx][ny] = -1 # 녹는 부분으로 체크
                else: # 공기일 경우
                    dq.append((nx, ny))

    return (existC, cheese)

r, c = map(int, input().split())
board = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(r):
    board.append(list(map(int, input().split())))

time = 0
lastCheese = 0
while 1:
    existC, curCheese = bfs()
    
    if not existC:
        print(time)
        print(lastCheese)
        break
    time += 1
    lastCheese = curCheese