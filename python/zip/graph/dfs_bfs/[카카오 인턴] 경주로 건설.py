# 전형적인 dfs 문제
# 상, 하, 좌, 우 (0, 1, 2, 3)
from collections import deque
import sys
INF = sys.maxsize

def dfs(board):
    n = len(board)
    dq = deque()
    dq.append((0, 0, 1, 0)) # x, y, 방향, cost
    dq.append((0, 0, 3, 0))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    dd = [0, 1, 2, 3]
    
    cost =[[[INF, INF, INF, INF] for _ in range(n)] for _ in range(n)]
    cost[0][0] = [0, 0, 0, 0]
    
    while dq:
        x, y, dir, c = dq.popleft()
        
        if cost[x][y][dir] < c:
            continue
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nd = dd[i]
            
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                nc = c + 100 if nd == dir else c + 600
                if cost[nx][ny][nd] > nc:
                    cost[nx][ny][nd] = nc
                    dq.append((nx, ny, nd, nc))

    return min(cost[-1][-1])

def solution(board):
    return dfs(board)