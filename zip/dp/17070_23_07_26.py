#파이프 옮기기1
#dp

#재귀
import sys
n = int(sys.stdin.readline())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dic = {
    0: [(0, 0, 1), (1, 1, 1)],
    1: [(0, 0, 1), (1, 1, 1), (2, 1, 0)],
    2: [(1, 1, 1), (2, 1, 0)]
}
result = 0

def dfs(type, x, y):
    global result
    if x == n-1 and y == n-1:
        result += 1
        return
    
    for type, dx, dy in dic[type]:
        nx = dx + x
        ny = dy + y
        if 0<=nx<n and 0<=ny<n:
            if(type == 0 and graph[x][y+1] == 0):
                dfs(type, nx, ny)
            elif(type == 1 and graph[x+1][y+1] == 0 and graph[x][y+1] == 0 and graph[x+1][y] == 0):
                dfs(type, nx, ny)
            elif(type == 2 and graph[x+1][y] == 0):
                dfs(type, nx, ny)

dfs(0, 0, 1)
print(result)

#덱
import sys
from collections import deque
n = int(sys.stdin.readline())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dic = {
    0: [(0, 0, 1), (1, 1, 1)],
    1: [(0, 0, 1), (1, 1, 1), (2, 1, 0)],
    2: [(1, 1, 1), (2, 1, 0)]
}

def dfs():
    result = 0
    deq = deque([(0, 0, 1)])
    
    while deq:
        type, x, y = deq.popleft()

        if type == 1 and (graph[x-1][y] == 1 or graph[x][y-1] == 1):
            continue

        if x == n-1 and y == n-1:
            result += 1
            continue

        for t, dx, dy in dic[type]:
            nx = dx + x
            ny = dy + y
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 0:
                deq.append((t, nx, ny))
        
    print(result)

dfs()

#dp
import sys

n = int(sys.stdin.readline())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dp_type1 = [[0]* n for _ in range(n)] # 좌
dp_type2 = [[0]* n for _ in range(n)] # 대각선
dp_type3 = [[0]* n for _ in range(n)] # 위
dp_type1[0][1] = 1

for i in range(n):
    for j in range(2, n):
        if graph[i][j] != 1:
            #대각선에서 올 경우
            if graph[i][j-1] != 1 and graph[i-1][j] != 1:
                dp_type2[i][j] += dp_type2[i-1][j-1] + dp_type1[i-1][j-1] + dp_type3[i-1][j-1]
            #좌에서 올 경우
            dp_type1[i][j] += dp_type2[i][j-1] + dp_type1[i][j-1]
            #위에서 올 경우
            dp_type3[i][j] += dp_type2[i-1][j] + dp_type3[i-1][j]

print(dp_type1[-1][-1] + dp_type2[-1][-1] + dp_type3[-1][-1])