#23.02.19
#벽 부수고 이동하기
#골드 3

#bfs
#이 문제에서의 핵심: 벽을 부수고 가는 경로와 벽을 부수지 않고 가는 경로의 visited를 분리해야 한다.
#벽을 부수고 간 경로는 다시 한 번 벽을 만났을 때 지나가지 못한다.
#벽을 부수고 가지 않은 경로는 해당 위치에서 벽을 만났을 때 벽을 뚫고 지나갈 수 있다.
#따라서 같은 위치더라도 벽을 부순 여부에 따라 이후 경로가 달라지기 때문에 visited을 분리해야 한다.
import sys
from collections import deque
INF = sys.maxsize

def bfs():
    global answer
    q = deque([(1, 0, 0, False)])
    visited1 = [[0]*m for _ in range(n)]
    visited2 = [[0]*m for _ in range(n)]
    visited1[0][0] = 1

    while q:
        dis, x, y, check = q.popleft()

        if x == n-1 and y == m-1:
            return dis

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == "0": # 벽이 아닐 경우
                    if not check: # 벽을 허물지 않고 지나가는 경우
                        if visited1[nx][ny] == 0:
                            visited1[nx][ny] = 1
                            q.append((dis+1, nx, ny, check))
                    else: # 벽을 허물고 지나가는 경우
                        if visited2[nx][ny] == 0:
                            visited2[nx][ny] = 1
                            q.append((dis+1, nx, ny, check))
                else: # 벽일 경우
                    if check == False:
                        q.append((dis+1, nx, ny, True))
    
    return -1

n, m = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
walls = []

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

print(bfs())