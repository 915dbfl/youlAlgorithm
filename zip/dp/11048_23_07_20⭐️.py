# 이동하기
#dp

# bfs: 시간초과
import sys
from collections import deque

n, m = map(int, input().split())
dx = [1, 1, 0]
dy = [0, 1, 1]

def bfs():
    global graph
    queue = deque([(0, 0)])
    # visited = [[0] * m for _ in range(n)]
    result = [[0] * m for _ in range(n)]
    result[0][0] = graph[0][0]

    while queue:
        x, y = queue.popleft()
        # if visited[x][y] == 0:
        #     visited[x][y] = 1

        for i in range(3):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                if result[nx][ny] == 0 or result[nx][ny] < result[x][y] + graph[nx][ny]:
                    queue.append((nx, ny))
                result[nx][ny] = max(result[nx][ny], result[x][y] + graph[nx][ny])
    
    print(result[-1][-1])


graph = []
for i in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    graph.append(lst)

bfs()

# dp
n, m = map(int, input().split())
dx = [-1, -1, 0]
dy = [0, -1, -1]

def getDP():
    for i in range(n):
        for j in range(m):
            if i != 0 or j != 0:
                
                Max = 0
                for k in range(3):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0<=nx<n and 0 <=ny<m:
                        Max = max(graph[nx][ny], Max)
                    
                graph[i][j] += Max

    print(graph[-1][-1])

graph = []
for i in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    graph.append(lst)

getDP()