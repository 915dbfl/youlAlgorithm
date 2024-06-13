# 42분
import sys
input = sys.stdin.readline

def rotate(c):
    x, y = c, c
    base = array[x][y]
    cur = -1
    for i in range(4):
        for _ in range(l[i]-2*c-1):
            nx = x + dx[i]
            ny = y + dy[i]
            cur = array[nx][ny]
            array[nx][ny] = base
            base = cur
            x, y = nx, ny
            

n, m, r = map(int, input().split())
array = []
circle = min(n, m) // 2
for _ in range(n):
    array.append(list(input().rstrip().split()))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
l = [n, m, n, m]
for c in range(circle):
    period = (n-2*c)*2 + (m-2*c)*2 - 4
    tmp_r = r % period
    for _ in range(tmp_r):
        rotate(c)

for i in range(n):
    print(" ".join(array[i]))

# ㅁ를 일차원 배열로 펼쳐 rotate 진행

NN, MM, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(NN)]

from collections import deque
depth = min(NN, MM)//2
move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for d in range(depth):
    r, c = d, d
    N = NN - d*2
    M = MM - d*2
    q = deque()
    for dr, dc in move:
        while True:
            nr, nc = r+dr, c+dc
            if d<=nr<d+N and d<=nc<d+M:
                q.append(arr[nr][nc])
                r, c = nr, nc
            else:
                break

    # rotate
    rotate = R % (2*(N-1)+2*(M-1))
    for _ in range(rotate):
        q.append(q.popleft())
    
    # write at arr
    for dr, dc in move:
        while True:
            nr, nc = r+dr, c+dc
            if d<=nr<d+N and d<=nc<d+M:
                arr[nr][nc] = q.popleft()
                r, c = nr, nc
            else:
                break

for row in arr:
    print(' '.join(map(str, row)))