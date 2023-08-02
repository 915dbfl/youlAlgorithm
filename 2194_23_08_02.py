# 유닛 이동시키기
# bfs

#오답
import sys
from collections import deque
n, m, a, b, k = map(int, input().split())
graph = [[0]*(m+1) for _ in range(n+1)]

for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1

xs, ys = map(int, input().split())
xe, ye = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    dq = deque()
    dq.append([xs, ys, 0])

    while dq:
        x, y, move = dq.popleft()
        
        if x == xe and y == ye:
            print(move)
            exit(0)

        if graph[x][y] != 1 and graph[x][y] != -1:
            graph[x][y] = -1

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                skip = False
                for j in range(a):
                    if 0<nx+j<=n and not skip: 
                        for k in range(b):
                            if 0<ny+k<=m:
                                if graph[nx+j][ny+k] == 1: # 장애물이 있을 경우
                                    skip = True
                                    break
                            else: # 범위를 넘어간 경우
                                skip = True
                                break
                    else: # 범위를 넘어간 경우
                        break
                else: # 이동할 수 있음
                    dq.append([nx, ny, move+1])
    
    print(-1)
bfs()
