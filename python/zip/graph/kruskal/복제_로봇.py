# 하나의 칸에 동시에 여러 로봇이 위치할 수 있음
# 동일한 곳을 여러번 지나갈 수 있음

# 모든 경우의 수를 파악한다.
# 시작, 열쇠 위치에서 다른 위치까지의 최소 거리 구하기 => O(M*N^2)
    # bfs -> 250 * 2500 -> 625000
# 최소 스패닝 트리로 연결 => O(ElogE)
    # 간선 전체 확인
    # 250 * 250 = 62500

import sys
from collections import deque, defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = sys.maxsize

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, board):
    dq = deque()
    dq.append([x, y, 0])

    visited = [[INF]*len(board) for _ in range(len(board))]
    visited[x][y] = 0

    while dq:
        cx, cy, dist = dq.popleft()

        if visited[cx][cy] < dist: continue

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0<=nx<len(board) and 0<=ny<len(board) and visited[nx][ny] > dist+1 and board[nx][ny] != "1":
                visited[nx][ny] = dist + 1
                dq.append([nx, ny, dist+1])

    for kx, ky in keys:
        if (kx != x or ky != y) and visited[kx][ky] != INF:
            edge.append([x, y, kx, ky, visited[kx][ky]])

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(input().rstrip()))

# 시작 위치와 열쇠 위치 구하기
keys = []
for i in range(n):
    for j in range(n):
        if board[i][j] == "K" or board[i][j] == "S":
            keys.append([i, j])

# bfs 진행, 최소스패닝트리를 위한 부모 저장
edge = []
parent = defaultdict(list)
for kx, ky in keys:
    dist = bfs(kx, ky, board)
    parent[(kx, ky)] = (kx, ky)

# 최소스패닝트리 진행
edge.sort(key = lambda x: x[4])

def find_parent(target):
    if parent[target] == target: 
        return target
    else: 
        return find_parent(parent[target])

def union(target1, target2):
    target1 = find_parent(target1)
    target2 = find_parent(target2)
    t1Lst = list(target1)
    t2Lst = list(target2)

    if t1Lst[0] < t2Lst[0]:
        parent[target2] = target1
    elif t1Lst[1] < t2Lst[1]:
        parent[target2] = target1
    else:
        parent[target1] = target2

answer = 0
for sx, sy, ex, ey, dist in edge:
    if dist == INF:
        break

    target1 = (sx, sy)
    target2 = (ex, ey)
    if find_parent(target1) != find_parent(target2):
        answer += dist
        union(target1, target2)

base = find_parent((keys[0][0], keys[0][1]))
for i in range(1, m+1):
    p = find_parent(tuple(keys[i]))
    if base != p:
        print(-1)
        break
else:
    print(answer)

# 다른 풀이
import sys
from collections import deque

input = sys.stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = list(map(int, input().rstrip().split()))
board = [list(input().rstrip()) for _ in range(n)]
parent = [i for i in range(m + 1)]
edges = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

cnt = 0
to_node = {}
temp = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 'S' or board[i][j] == 'K':
            # 배울 점⭐️: 좌표를 하나의 Index로 바꿔서 사용
            to_node[(i, j)] = cnt
            cnt += 1
            temp.append((i, j))

q = deque()
for k in temp:
    q.append((k[0], k[1]))
    check = [[-1] * n for _ in range(n)]
    check[k[0]][k[1]] = 0
    while q:
        px, py = q.popleft()
        for i in range(4):
            nx, ny = px + dx[i], py + dy[i]
            if (0 <= nx < n) and (0 <= ny < n) and (board[nx][ny] != '1') and (check[nx][ny] == -1):
                check[nx][ny] = check[px][py] + 1
                q.append((nx, ny))
    for i in temp:
        if check[i[0]][i[1]] > 0:
            edges.append((check[i[0]][i[1]], to_node[k], to_node[i]))

edges.sort()
res, mst = 0, 0
for edge in edges:
    if res == m: break
    if find(edge[1]) != find(edge[2]):
        union(edge[1], edge[2])
        res += 1
        mst += edge[0]

if res == m:
    print(mst)
else:
    print(-1)