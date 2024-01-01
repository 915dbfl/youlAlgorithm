# 봄버맨

# 최대 10**6이므로 전체 배열을 돌며 폭탄을 설치하고 폭파 처리를 한다.
# 해당 풀이 문제점
    # 기존에 폭탄이 있었지만 이전 폭탄으로 .으로 바뀌게 되면 해당 자리는 폭탄이 없었던 것처럼 취급된다.
import sys

r, c, n = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bomb = "O"
for _ in range(n):

    for i in range(r):
        for j in range(c):
            if graph[i][j] == ".":
                graph[i][j] = "1" if bomb == "O" else "O"

    for row in graph:
        print(row)
    print("**********************")
    
    for l in range(r):
        for m in range(c):
            if graph[l][m] == bomb:
                graph[l][m] = "."
                for k in range(4):
                    nx = l+dx[k]
                    ny = m+dy[k]

                    if 0<=nx<r and 0<=ny<c:
                        graph[nx][ny] = "."

    for row in graph:
        print(row)
    print("==================================")

    bomb = "O" if bomb == "1" else "1"

for row in graph:
    str = "".join(row).replace(bomb, "O")
    print(str)

# 단순 구현
# 10**8이지만 간신히 통과한 느낌!
import sys

r, c, n = map(int, sys.stdin.readline().split())
graph = []
bomb = [[0]* c for _ in range(r)]

for i in range(r):
    lst = list(sys.stdin.readline().rstrip())
    for j in range(c):
        if lst[j] == "O":
            bomb[i][j] = 1
    graph.append(lst)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 1
while 1:
    if time == n:
        break

    for i in range(r):
        for j in range(c):
            graph[i][j] = "O"

    time += 1
    if time == n:
        break
    
    for i in range(r):
        for j in range(c):
            if bomb[i][j] == 1:
                graph[i][j] = "."

                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if 0<=nx<r and 0<=ny<c:
                        graph[nx][ny] = "."

    for i in range(r):
        for j in range(c):
            if graph[i][j] == "O":
                bomb[i][j] = 1
            else:
                bomb[i][j] = 0

    time += 1

for row in graph:
    print("".join(row))

# 코드 분리
import sys
input = sys.stdin.readline
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]
q = deque()

R,C,N = map(int,input().rstrip().split())

board = []
for _ in range(R):
    board.append(list(input().rstrip()))

# 폭탄 폭발
def bfs(q,board):
    while q:
        x,y = q.popleft()
        board[x][y] = '.'
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if nx>=0 and nx<R and ny>=0 and ny<C and board[nx][ny] =='O':
                board[nx][ny] = '.'

def simulate(t):
    global q, board
    if t == 1:
        # 제일 처음 폭탄 위치 저장
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    q.append((i,j))
    elif t%2 == 1:
        # 3초가 지난 폭탄을 폭발시킨다.
        bfs(q,board)
        # 3초후에 터질 폭탄을 q에 다시 저장한다.
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    q.append((i,j))
    else:
        # 모든 칸에 폭탄 설치
        board = [['O']*C for _ in range(R)]

for i in range(1,N+1):
    simulate(i)

for i in board:
    print(''.join(i))