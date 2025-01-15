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