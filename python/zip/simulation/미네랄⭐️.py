import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
graph = []

for _ in range(r):
    graph.append(list(input().rstrip()))

n = int(input())
hlist = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def destroy_mi(y, turn):
    # 오른쪽부터
    if turn % 2 == 1:
        for i in range(c-1, -1, -1):
            if graph[y][i] == "x":
                graph[y][i] = "."
                break
    # 왼쪽부터
    else:
        for i in range(c):
            if graph[y][i] == "x":
                graph[y][i] = "."
                break

def find_cluster(graph):
    visited = [[False] * c for _ in range(r)]
    q = deque()

    for i in range(c):
        if graph[-1][i] == "x":
            q.append((r-1, i))
            visited[r-1][i] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<r and 0<=ny<c and not visited[nx][ny] and graph[nx][ny] == "x":
                visited[nx][ny] = True
                q.append((nx, ny))

    cluster = []
    for i in range(r-1, -1, -1):
        for j in range(c):
            if graph[i][j] == "x" and not visited[i][j]:
                cluster.append((i, j))

    return cluster, visited

def move_cluster(cluster, visited):
    down_min = 1e9

    for x, y in cluster:
        down_cnt = 0
        for i in range(x+1, r):
            if graph[i][y] == ".":
                down_cnt += 1
            if graph[i][y] == "x" and visited[i][y] == True:
                break
        down_min = min(down_min, down_cnt)

    for x, y in cluster:
        graph[x][y] = "."
        graph[x+down_min][y] = "x"
    
    return graph

for i in range(n):
    # 1. 미네랄 파괴
    destroy_mi(r-hlist[i], i)
    # 2. 클러스터 조사
    cluster, visited = find_cluster(graph)
    # 3. 클러스터 이동
    if len(cluster) > 0:
        move_cluster(cluster, visited)

for i in range(r):
    print("".join(graph[i]))