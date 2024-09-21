# 시간 및 메모리 초과
import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize

n, m, k = map(int, input().split())
maps = [list(input().rstrip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dist = [[INF] * m for _ in range(n)]

answer = INF

def bfs():
    global answer
    dq = deque()
    dist[0][0] = 1
    dq.append((0, 0, 1, k))

    while dq:
        cx, cy, cd, cntK = dq.popleft()

        if cx == n-1 and cy == m-1:
            answer = min(answer, cd)
            return

        if dist[cx][cy] < cd:
            continue

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < m and cd + 1 <= dist[nx][ny]:
                dist[nx][ny] = cd + 1
                if maps[nx][ny] == "1" and cntK > 0:
                    dq.append((nx, ny, cd + 1, cntK - 1))
                if maps[nx][ny] == "0":
                    dq.append((nx, ny, cd + 1, cntK))


bfs()
print(answer if answer < INF else -1)

# 삼차원 배열 풀이

import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
maps = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

visited = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]
visited[0][0][k] = 1

def bfs():
    dq = deque()
    dq.append((0, 0, k))

    while dq:
        cx, cy, ck = dq.popleft()

        if cx == n-1 and cy == m-1:
            return visited[cx][cy][ck]
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if not (0 <= nx < n) or not (0 <= ny < m):
                continue

            if maps[nx][ny] == 1 and ck > 0 and visited[nx][ny][ck-1] == 0:
                visited[nx][ny][ck-1] = visited[cx][cy][ck] + 1
                dq.append((nx, ny, ck-1))
            elif maps[nx][ny] == 0 and visited[nx][ny][ck] == 0:
                visited[nx][ny][ck] = visited[cx][cy][ck] + 1
                dq.append((nx, ny, ck))

    return -1

print(bfs())