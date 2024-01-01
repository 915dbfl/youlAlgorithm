#배열탈출

#bfs, dfs
import sys
from collections import deque
n = int(input())
graph = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))

def bfs():
    dq = deque()
    dq.append([0, 0, 0])

    Min = n*n*222
    dx = [1, 0]
    dy = [0, 1]

    while dq:
        x, y, cost = dq.popleft()

        if x == n-1 and y == n-1:
            Min = min(Min, cost)

        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[x][y] <= graph[nx][ny]:
                    cost += graph[nx][ny] - graph[x][y] + 1

                if cost < Min:
                    dq.append([nx, ny, cost])

    print(Min)

bfs()

#dp
import sys
from collections import deque
n = int(input())
graph = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))

dp = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        preR = preC = sys.maxsize
        if i == 0 and j == 0:
            continue
        if i-1 >= 0:
            preR = dp[i-1][j] + (graph[i][j] - graph[i-1][j] + 1 if graph[i][j] >= graph[i-1][j] else 0)
        if j-1 >= 0:
            preC = dp[i][j-1] + (graph[i][j] - graph[i][j-1] + 1 if graph[i][j] >= graph[i][j-1] else 0)
        dp[i][j] = min(preR, preC)

print(dp[-1][-1])