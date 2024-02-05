# bfs 풀이
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    dq = deque()
    if visited[x][y][0] == 0:
        dq.append((x, y, 0, board[x][y]))
        visited[x][y][0] = 1
    if visited[x][y][1] == 0:
        dq.append((x, y, 1, board[x][y]))
        visited[x][y][1] = 1

    while dq:
        curx, cury, dir, str = dq.popleft()

        if dir == 0: # 오른쪽으로 단어가 이어질 경우
            nx = curx + dx[0]
            ny = cury + dy[0]
            
        else: # 아래쪽으로 단어가 이어질 경우
            nx = curx + dx[1]
            ny = cury + dy[1]

        # 범위내에 있고 
        if 0 <= nx < r and 0 <= ny < c:
            # 해당 방향으로 방문하지 않았을 경우
            if visited[nx][ny][dir] == 0:
                # 막혀있지 않다면
                if board[nx][ny] != "#":
                    visited[nx][ny][dir] = 1
                    dq.append((nx, ny, dir, str + board[nx][ny]))
                else:
                    if len(str) > 1:
                        dic.append(str)
        else:
            if len(str) > 1:
                dic.append(str)
            

r, c = map(int, input().split())
board = []
dic = []

dx = [0, 1]
dy = [1, 0]

for _ in range(r):
    board.append(list(input().rstrip()))

visited = [[[0 for _ in range(2)] for _ in range(c)] for _ in range(r)]
for i in range(r):
    for j in range(c):
        if (visited[i][j][0] == 0 or visited[i][j][1] == 0) and board[i][j] != "#":
            bfs(i, j)

dic.sort()
print(dic[0])

# 문자열 
import sys
input = sys.stdin.readline

def splitAndAdd(base):
    for b in base:
        for word in b.split("#"):
            if len(word) > 1:
                dic.append(word)

r, c = map(int, input().split())
matrix_row = []
for _ in range(r):
    matrix_row.append(input().rstrip())

matrix_col = list(''.join(case) for case in zip(*matrix_row))

dic = []
splitAndAdd(matrix_row)
splitAndAdd(matrix_col)

dic.sort()
print(dic[0])