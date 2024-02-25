# 시간 초과
import sys
from collections import deque
input = sys.stdin.readline

def bfs(gx, gy):
    dq = deque()
    dq.append((x, y, 0))
    visited = [[0 for _ in range(n+1)] for _ in range(n+1)]
    visited[x][y] = 1

    while dq:
        cx, cy, dis = dq.popleft()

        if cx == gx and cy == gy:
            return dis

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0<nx<=n and 0<ny<=n and visited[nx][ny] == 0:
                if Map[nx-1][ny-1] == 0:
                    visited[nx][ny] = 1
                    dq.append((nx, ny, dis+1))
    return -1

def isPossible(usage):
    return f - usage >= 0

n, m, f = map(int, input().split())

Map = []
for _ in range(n):
    Map.append(list(map(int, input().split())))

x, y = map(int, input().split())

client = set()
for _ in range(m):
    sx, sy, gx, gy = map(int, input().split())
    client.add((sx, sy, gx, gy))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while len(client) > 0:
    targetXY = (n, n, n, n)
    toStartDis = sys.maxsize

    for sx, sy, gx, gy in client:
        tmpDis = bfs(sx, sy)
    
        if tmpDis != -1: # 이동할 수 있는 거리인지 확인
            if toStartDis > tmpDis: # 최단거리가 더 짧은지 확인
                targetXY = (sx, sy, gx, gy)
                toStartDis = tmpDis
            elif toStartDis == tmpDis: # 최단거리가 동일하다면 행 확인
                if targetXY[0] > sx:
                    targetXY = (sx, sy, gx, gy)
                elif targetXY[0] == sx: # 최단거리, 행이 모두 동일하다면 열 확인
                    if targetXY[1] > sy:
                        targetXY = (sx, sy, gx, gy)

    if not isPossible(toStartDis): # 최단거리 출발지로 이동하지 못하는 경우
        f -= toStartDis
        print(-1)
        break
    
    f -= toStartDis
    x, y = targetXY[0], targetXY[1]
    toGoalDis = bfs(targetXY[2], targetXY[3])

    if not isPossible(toGoalDis): # 목적지로 이동하지 못하는 경우
        f -= toGoalDis
        print(-1)
        break

    f += toGoalDis
    x, y = targetXY[2], targetXY[3]
    client = client - set([targetXY]) # 해당 승객 리스트에서 제외

if f >= 0:
    print(f)

# 매 단계 bfs를 두 번만 진행
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    dq = deque()
    dq.append((x, y, 0))

    while dq:
        cx, cy, dis = dq.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0<nx<=n and 0<ny<=n and visited[nx][ny] == -1:
                if Map[nx-1][ny-1] == 0:
                    visited[nx][ny] = dis + 1
                    dq.append((nx, ny, dis+1))

def isPossible(usage):
    return f - usage >= 0

n, m, f = map(int, input().split())

Map = []
for _ in range(n):
    Map.append(list(map(int, input().split())))

x, y = map(int, input().split())

client = set()
for _ in range(m):
    sx, sy, gx, gy = map(int, input().split())
    client.add((sx, sy, gx, gy))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[-1 for _ in range(n+1)] for _ in range(n+1)]
visited[x][y] = 0

while len(client) > 0:
    targetXY = (n, n, n, n)
    toStartDis = sys.maxsize

    # 현재 택시 위치에서 최단 경로를 표시할 이차원 배열
    visited = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    visited[x][y] = 0

    bfs() # 현재 택시 위치에서 모든 위치 최단 경로 구하기

    for sx, sy, gx, gy in client:
        tmpDis = visited[sx][sy]
    
        if tmpDis != -1: # 이동할 수 있는 거리인지 확인
            if toStartDis > tmpDis: # 최단거리가 더 짧은지 확인
                targetXY = (sx, sy, gx, gy)
                toStartDis = tmpDis
            elif toStartDis == tmpDis: # 최단거리가 동일하다면 행 확인
                if targetXY[0] > sx:
                    targetXY = (sx, sy, gx, gy)
                elif targetXY[0] == sx: # 최단거리, 행이 모두 동일하다면 열 확인
                    if targetXY[1] > sy:
                        targetXY = (sx, sy, gx, gy)

    if not isPossible(toStartDis): # 최단거리 출발지로 이동하지 못하는 경우
        f -= toStartDis
        print(-1)
        break
    
    f -= toStartDis
    x, y = targetXY[0], targetXY[1]

    # 현재 택시 위치에서 최단 경로를 표시할 이차원 배열
    visited = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    visited[x][y] = 0
    bfs() # 변경된 택시 위치에서 최단 경로 구하기
    toGoalDis = visited[targetXY[2]][targetXY[3]]

    if toGoalDis == -1 or not isPossible(toGoalDis): # 목적지로 이동하지 못하는 경우
        f -= sys.maxsize
        print(-1)
        break

    f += toGoalDis
    x, y = targetXY[2], targetXY[3]
    client = client - set([targetXY]) # 해당 승객 리스트에서 제외

if f >= 0:
    print(f)