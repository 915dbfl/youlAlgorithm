# 84분

"""
해당 반례는 클러스터가 분리되어 있어 잘못된 반례이지만
움직일 수 있는 count를 구하는 방식과 관련해 고려해볼만한 반례이다.

9 8
........
.xxxx...
.x......
.x.xxxx.
.x....x.
.x....x.
.xxxx.x.
....xxx.
......x.
1
2

output:
........
........
.xxxx...
.x.xxxx.
.x....x.
.x....x.
.x....x.
.xxxxxx.
......x.
"""

import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
cave = []
mineral = 0

for _ in range(r):
    col = list(input().rstrip())
    mineral += col.count('x')
    cave.append(col)

turnCnt = int(input())
heights = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def throw(height, isLeft):
    # 리팩토링 필요
    if isLeft:
        for i in range(c):
            if cave[r-height][i] == 'x':
                destroy(r-height, i)
                return
    else:
        for i in range(c-1, -1, -1):
            if cave[r-height][i] == 'x':
                destroy(r-height, i)
                return

def destroy(x, y):
    global mineral
    cave[x][y] = '.'
    mineral -= 1
    checkFall()

def checkFall():
    # 클러스터가 분리되었다면
    isDivided, visited = checkDivide()
    if isDivided:
        fall(visited)

def fall(visited):
    moveCnt = r

    # 가능한 최대의 움직임 구하기
    for i in range(c):
        moveCnt = min(moveCnt, checkMoveCnt(i, visited))
    
    move(moveCnt, visited)

def move(cnt, visited):
    for i in range(c):
        for j in range(r-1, -1, -1):
            if cave[j][i] == 'x' and not visited[j][i]:
                cave[j][i] = '.'
                cave[j+cnt][i] = 'x'

def checkMoveCnt(col, visited):
    bottomMineralTop = r
    topMineralBottom = 0
    canMove = r
    for i in range(r-1, -1, -1):
        if cave[i][col] == 'x':
            if visited[i][col]:
                bottomMineralTop = i
            else:
                topMineralBottom = i
                canMove = min(canMove, abs(bottomMineralTop - topMineralBottom) - 1)
    return canMove

def checkDivide():
    bottomMineral = 0
    visited = [[False] * c for _ in range(r)]
    for i in range(c):
        if cave[r-1][i] == 'x' and not visited[r-1][i]:
            clusterMineral = dfs(r-1, i, visited)
            bottomMineral += clusterMineral
    
    return mineral != bottomMineral, visited

def dfs(x, y, visited):
    dq = deque([(x, y)])
    visited[x][y] = True
    cluster = 1
    
    while dq:
        curx, cury = dq.popleft()

        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]

            if 0<=nx<r and 0<=ny<c:
                if cave[nx][ny] == 'x' and not visited[nx][ny]:
                    cluster += 1
                    visited[nx][ny] = True
                    dq.append((nx, ny))

    return cluster

for i in range(turnCnt):
    if i % 2 == 0:
        throw(heights[i], 1)
    else:
        throw(heights[i], 0)

for row in cave:
    print("".join(row))