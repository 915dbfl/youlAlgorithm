# 다익스트라
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

m, n = map(int, input().split())
miro = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = n*m + 1

def dijkstra():
    global answer
    hq = []
    visited = [[-1] * m for _ in range(n)]
    heappush(hq, (0, 0, 0))
    visited[0][0] = 0

    while hq:
        breakCnt, cx, cy = heappop(hq)

        if cx == n-1 and cy == m-1:
            print(breakCnt)
            exit(0)

        if visited[cx][cy] < breakCnt: continue

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0<=nx<n and 0<=ny<m:
                nBreakCnt = breakCnt + 1 if miro[nx][ny] == 1 else breakCnt
                if visited[nx][ny] == -1 or visited[nx][ny] > nBreakCnt:
                    visited[nx][ny] = nBreakCnt
                    heappush(hq, (nBreakCnt, nx, ny))

dijkstra()