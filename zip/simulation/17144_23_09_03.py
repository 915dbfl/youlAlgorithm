# 미세먼지 안녕!

import sys

R, C, T = map(int, sys.stdin.readline().split())
room = []
findD = 0
airC = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(R):
    r = list(map(int, sys.stdin.readline().split()))
    for j in range(C):
        if r[j] >= 0:
            findD += r[j]
        elif r[j] == -1:
            airC.append((i, j))
    room.append(r)

def spread():
    spreadRoom = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                tmp = room[i][j]//5
                if tmp >= 1:
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if 0<=nx<R and 0<=ny<C and room[nx][ny] != -1:
                            spreadRoom[nx][ny] += tmp
                            spreadRoom[i][j] -= tmp

    for i in range(R):
        for j in range(C):
            if room[i][j] != -1:
                room[i][j] += spreadRoom[i][j]

for t in range(T):
    spread()
    ax, ay = airC[0]
    tmp1 = tmp2 = 0
    for i in range(ay+1, C):
        tmp2 = room[ax][i]
        room[ax][i] = tmp1
        tmp1 = tmp2

    for i in range(ax-1, -1, -1):
        tmp2 = room[i][-1]
        room[i][-1] = tmp1
        tmp1 = tmp2

    for i in range(C-2, -1, -1):
        tmp2 = room[0][i]
        room[0][i] = tmp1
        tmp1 = tmp2

    for i in range(1, ax):
        tmp2 = room[i][0]
        room[i][0] = tmp1
        tmp1 = tmp2

    findD -= tmp1

    ax, ay = airC[1]
    tmp1 = tmp2 = 0
    for i in range(ay+1, C):
        tmp2 = room[ax][i]
        room[ax][i] = tmp1
        tmp1 = tmp2

    for i in range(ax+1, R):
        tmp2 = room[i][-1]
        room[i][-1] = tmp1
        tmp1 = tmp2

    for i in range(C-2, -1, -1):
        tmp2 = room[-1][i]
        room[-1][i] = tmp1
        tmp1 = tmp2
    
    for i in range(R-2, ax, -1):
        tmp2 = room[i][0]
        room[i][0] = tmp1
        tmp1 = tmp2
    
    findD -= tmp1

print(findD)