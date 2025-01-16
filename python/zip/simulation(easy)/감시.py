# 1시간
# 최적화 필요
import sys
from itertools import product
input = sys.stdin.readline

def watch(curx, cury, diffx, diffy):
    global n, m
    while 0 <= curx < n and 0 <= cury < m and watch_info[curx][cury] != 6:
        if watch_info[curx][cury] == 0:
            watch_info[curx][cury] = -1
        curx += diffx
        cury += diffy

def check_watch(dirs):
    dir_idx = 0
    for i in range(n):
        for j in range(m):
            if dir_idx >= len(dirs):
                return
            cctv_num = cctv_info[i][j]
            dir = dirs[dir_idx]
            if cctv_num == 1:
                watch(i, j, dx[dir], dy[dir])
                dir_idx += 1
            elif cctv_num == 2:
                op_dir = (dir + 2) % 4
                watch(i, j, dx[dir], dy[dir])
                watch(i, j, dx[op_dir], dy[op_dir])
                dir_idx += 1
            elif cctv_num == 3:
                nxt_dir = (dir + 1) % 4
                watch(i, j, dx[dir], dy[dir])
                watch(i, j, dx[nxt_dir], dy[nxt_dir])
                dir_idx += 1
            elif cctv_num == 4:
                nxt_dir = (dir + 1) % 4
                nnxt_dir = (dir + 2) % 4
                watch(i, j, dx[dir], dy[dir])
                watch(i, j, dx[nxt_dir], dy[nxt_dir])
                watch(i, j, dx[nnxt_dir], dy[nnxt_dir])
                dir_idx += 1
            elif cctv_num == 5:
                nxt_dir = (dir + 1) % 4
                nnxt_dir = (dir + 2) % 4
                nnnxt_dir = (dir + 3) % 4
                watch(i, j, dx[dir], dy[dir])
                watch(i, j, dx[nxt_dir], dy[nxt_dir])
                watch(i, j, dx[nnxt_dir], dy[nnxt_dir])
                watch(i, j, dx[nnnxt_dir], dy[nnnxt_dir])
                dir_idx += 1

def check_blind():
    blind_spot = 0
    for row in watch_info:
        blind_spot += row.count(0)
    return blind_spot
            
n, m = map(int ,input().split())
cctv_info = []
for _ in range(n):
    cctv_info.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cctv_cnt = 0
for i in range(n):
    for j in range(m):
        if cctv_info[i][j] not in [0, 6]:
            cctv_cnt += 1

watch_info = [row[:] for row in cctv_info]
dir_list = range(4)
answer = sys.maxsize
for dirs in product(dir_list, repeat = cctv_cnt):
    check_watch(list(dirs))
    answer = min(answer, check_blind())
    watch_info = [row[:] for row in cctv_info]

print(answer)

"""
[최적화 풀이]
1. cctv별로 확인해야 하는 방향 지정
2. cctv 위치 저장
3. 모든 cctv - 모든 방향 dfs
"""

n, m = map(int, input().split())
office = []
cctv = []
blank = 0
answer = n*m + 1

# cctv 정보 저장 / blank 개수 카운트
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] != 0 and line[j] != 6:
            cctv.append([i, j, line[j]])
        elif line[j] == 0:
            blank += 1
    office.append(line)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# cctv별로 확인해야 하는 방향 리스트
# 필요한 방향만 확인함으로써 불필요한 반복 제거
dir = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

def move(x, y, dir_list):
    visited = []
    # 가능한 모든 방향 화인
    for d in dir_list:
        nx = x
        ny = y
        
        # 벽을 만날 때까지 반복
        while True:
            nx += dx[d]
            ny += dy[d]
            # 범위를 벗어나거나 벽을 만나면 정지!
            if not (0<=nx<n and 0<=ny<m) or office[nx][ny] == 6:
                break

            # 확인 표시
            if office[nx][ny] == 0:
                visited.append((nx, ny))
                office[nx][ny] = -1
    return visited

def undo_move(visited):
    for x, y in visited:
        office[x][y] = 0

def dfs(idx, blank):
    global answer
    # 모든 cctv를 확인한 경우
    if idx == len(cctv):
        answer = min(answer, blank)
        return
    
    # idx 번째 cctv 확인
    for dir_list in dir[cctv[idx][2]]:
        visited = move(cctv[idx][0], cctv[idx][1], dir_list)
        dfs(idx+1, blank - len(visited))
        # 백트래킹
        undo_move(visited)

dfs(0, blank)
print(answer)