# 주의할 요구사항
# 파란 구슬을 구멍에 넣지 않으면서 빨간 구슬을 10번 이하로 움직여서 빼낼 수 있으면 1을 없으면 0을 출력한다.

# 오답

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
visited = [[[[False, False, False, False] for _ in range(2)] for _ in range(m)] for _ in range(n)]

red = [-1, -1]
blue = [-1, -1]

# O(n*m) = 100
for i in range(n):
    for j in range(m):
        if board[i][j] == "B":
            blue = [i, j]
        elif board[i][j] == "R":
            red = [i, j]

dq = deque()
dq.append([red[0], red[1], blue[0], blue[1], 0])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
checkXY = [1, 1, 0, 0]

def startRoll(dir, red, blue):
    check = checkXY[dir]
    rx, ry, bx, by, checkR, checkB = -1, -1, -1, -1, False, False
    isRedFirst = False

    # 해당 방향으로 굴릴 때 순서가 영향을 미치는 경우
    if red[check] == blue[check]:
        # 값이 더 작을 떄 먼저 굴러감
        if dir in set([0, 2]):
            if red[1-check] < blue[1-check]:
                isRedFirst = True
                rx, ry, checkR = roll(red, dir, blue[0], blue[1])
                bx, by, checkB = roll(blue, dir, rx, ry)
            else:
                bx, by, checkB = roll(blue, dir, red[0], red[1])
                rx, ry, checkR = roll(red, dir, bx, by)
        # 값이 더 클 떄 먼저 굴러감
        else:
            if red[1-check] < blue[1-check]:
                bx, by, checkB = roll(blue, dir, red[0], red[1])
                rx, ry, checkR = roll(red, dir, bx, by)
            else:
                isRedFirst = True
                rx, ry, checkR = roll(red, dir, blue[0], blue[1])
                bx, by, checkB = roll(blue, dir, rx, ry)
    # 위치 순서가 상관 없는 경우
    else:
        isRedFirst = True
        rx, ry, checkR = roll(red, dir, blue[0], blue[1])
        bx, by, checkB = roll(blue, dir, rx, ry)

    return rx, ry, bx, by, checkR, checkB, isRedFirst

def roll(cur, dir, anotherDiceX, anotherDiceY):
    x, y = cur
    ansX, ansY = x, y
    canOut = False

    while board[x][y] != "#" and (x != anotherDiceX or y != anotherDiceY):
        ansX, ansY = x, y
        x += dx[dir]
        y += dy[dir]
        if board[x][y] == "O":
            canOut = True      

    return ansX, ansY, canOut

def setNewDice(rx, ry, bx, by):
    board[red[0]][red[1]] = "."
    board[blue[0]][blue[1]] = "."
    board[rx][ry] = "R"
    board[bx][by] = "B"

while dq:
    redX, redY, blueX, blueY, cnt = dq.popleft()

    if (cnt > 10): continue
    if board[redX][redY] == "O":
        print(1)
        break

    for i in range(4):
        # 두 구슬 모두 갔다왔던 길이라면
        if visited[redX][redY][0][i] and visited[blueX][blueY][1][i]:
            continue
        visited[redX][redY][0][i] = True
        visited[blueX][blueY][1][i] = True
        setNewDice(redX, redY, blueX, blueY)
        nrx, nry, nbx, nby, checkR, checkB, isRedFirst = startRoll(i, [redX, redY], [blueX, blueY])

        # red와 blue의 위치가 서로 달라야 함
        if nrx == nbx and nry == nby: continue
        # red가 구멍에 먼저 빠지는 경우
        if checkR:
            if not checkB:
                print(1)
                exit(0)

        # blue가 구멍에 먼저 빠지는 경우
        if not isRedFirst and checkB:
            continue
    
        dq.append([nrx, nry, nbx, nby, cnt+1])
        setNewDice(red[0], red[1], blue[0], blue[1])

print(0)

# 다른 풀이
# 시간 복잡도: O((n*m) ^ 2) = 10000
# bfs 최악의 경우, 모든 상태를 한 번씩 탐색해야 한다.

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()

def pos_init():
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                rx, ry = i, j
            elif board[i][j] == "B":
                bx, by = i, j

    queue.append((rx, ry, bx, by, 0))
    visited[rx][ry][bx][by] = True

def move(x, y, dx, dy):
    cnt = 0
    
    # 다음이 벽이거나 현재가 구멍일 때까지 이동
    while 1:
        if board[x+dx][y+dy] == '#' or board[x][y] == 'O':
            return x, y, cnt
        x += dx
        y += dy
        cnt += 1

def solve():
    pos_init()
    while queue:
        rx, ry, bx, by, depth = queue.popleft()

        if depth > 10:
            break

        if board[rx][ry] == "O":
            print(1)
            return

        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])

            if board[nbx][nby] == "O":
                continue

            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                queue.append((nrx, nry, nbx, nby, depth + 1))
    print(0)

solve()