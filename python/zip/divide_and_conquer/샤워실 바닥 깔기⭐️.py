# 분할 정복

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

k = int(input())
x, y = map(int, input().split())
num = 1

x, y = 2**k - y, x - 1
tile = [[0] * 2**k for _ in range(2**k)]
tile[x][y] = -1

def setTile(r, c, k, area):
    global num
    cnt = 3
    if k == 1:
        if area == 0 or area == 4:
            for i in range(r, r+2):
                for j in range(c, c+2):
                    if tile[i][j] == 0 and cnt > 0:
                        cnt -= 1
                        tile[i][j] = num
        elif area == 1:
            for i in range(r+1, r-1, -1):
                for j in range(c, c+2):
                    if tile[i][j] == 0 and cnt > 0:
                        cnt -= 1
                        tile[i][j] = num
        elif area == 2:
            for i in range(r, r+2):
                for j in range(c+1, c-1, -1):
                    if tile[i][j] == 0 and cnt > 0:
                        cnt -= 1
                        tile[i][j] = num
        elif area == 3:
            for i in range(r+1, r-1, -1):
                for j in range(c+1, c-1, -1):
                    if tile[i][j] == 0 and cnt > 0:
                        cnt -= 1
                        tile[i][j] = num
        num += 1
        return

    setTile(r, c, k-1, 0)
    setTile(r + 2**(k-1), c, k-1, 1)
    setTile(r, c + 2**(k-1), k-1, 2)
    setTile(r + 2**(k-1), c + 2**(k-1), k-1, 3)
    setTile(r + 2**k//4, c + 2**k//4, k-1, 4)

setTile(0, 0, k, 0)

for i in range(2**k):
    for j in range(2**k):
        print(tile[i][j], end = " ")
    print()
    