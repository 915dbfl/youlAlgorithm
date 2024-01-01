# 인구 이동

# dfs로 union 찾기
# 한 time에 전체 union을 찾고
# union끼리 update할 값을 구해 update를 진행한다.
# 한 time에 union이 더 이상 없을 때까지 반복한다.

import sys
from collections import deque

n, l, r = map(int, sys.stdin.readline().split())
countries = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cntM = 0

for _ in range(n):
    countries.append(list(map(int, sys.stdin.readline().split())))

def checkDiff(x, y, nx, ny):
    return l <= abs(countries[x][y] - countries[nx][ny]) <= r

def dfs(x, y):
    global cntM
    dq = deque()
    dq.append((x, y))
    union_tmp = set([(x, y)])

    while dq:
        row, col = dq.pop()
        
        if visited[row][col] == 0:
            visited[row][col] = 1

            for i in range(4):
                nx = row + dx[i]
                ny = col + dy[i]

                if 0<=nx<n and 0<=ny<n:
                    if checkDiff(row, col, nx, ny):
                        union_tmp.add((nx, ny))
                        if visited[nx][ny] == 0:
                            dq.append((nx, ny))

    return union_tmp

cnt = 0
while 1:
    visited = [[0]* 50 for _ in range(50)]
    unions = []
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                tmp = dfs(i, j)
                if len(tmp) > 1:
                    unions.append(tmp)

    if len(unions) != 0:
        cnt += 1
        for union in unions:
            sum = 0
            for cx, cy in union:
                sum += countries[cx][cy]

            sum //= len(union)
            for cx, cy in union:
                countries[cx][cy] = sum
    else:
        break         

print(cnt)