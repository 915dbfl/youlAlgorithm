# 최소 명령 횟수 -> bfs
# 문제 제대로 읽기: 직선 이동은 최대 3칸이 가능하다.
import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
graph = []

for i in range(m):
    graph.append(list(map(int, sys.stdin.readline().split())))

# 행, 열, 방향
start = list(map(int, input().split()))
end = list(map(int, input().split()))

# 동서남북 순서대로 이동 시 변화하는 좌표 diff 저장
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# 각 방향에서 left할 때 순서 저장
left = [
    [0, 3, 1, 2],
    [1, 2, 0, 3],
    [2, 0, 3, 1],
    [3, 1, 2, 0]
]

def bfs(start, end):
    dq = deque([[start[0]-1, start[1]-1, start[2]-1, 0]])
    visited = [[0] * n for _ in range(m)]
    visited[start[0]-1][start[1]-1] = 1

    while dq:
        # 현재 x, 현재 y, 현재 방향, 지금까지 명령 횟수
        cx, cy, dir, ord = dq.popleft()
        print(cx, cy, dir, ord)

        # 원하는 위치로 이동을 완료했을 때
        if(cx+1 == end[0] and cy+1 == end[1]):
            if (dir+1 == end[2]):
                print(ord)
            else:
                if left[dir][1]+1 == end[2] or left[dir][3]+1 == end[2]:
                    print(ord+1)
                elif left[dir][2]+1 == end[2]:
                    print(ord+2)
            return
        
        # 원하는 위치가 아닐 경우
        for i in range(4):
            nd = left[dir][i] # 방향 전환
            nx = cx
            ny = cy
            for _ in range(3): # 방향 전환 후 1, 2, 3칸 이동
                nx = nx + dx[nd]
                ny = ny + dy[nd]
                if 0<= nx < m and 0 <= ny < n: # graph 범위 내일 경우
                    if graph[nx][ny] == 0 and visited[nx][ny] == 0: # 궤도가 존재할 경우
                        if i < 3:
                            dq.append([nx, ny, nd, ord+1+i])
                        elif i == 3:
                            dq.append([nx, ny, nd, ord+2])
                        visited[nx][ny] = 1

bfs(start, end)