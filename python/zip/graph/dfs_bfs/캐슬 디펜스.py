"""
풀이 과정
1. 궁수의 위치
    - m 중 3군데(m <= 15)
    - combination 활용
2. 궁수가 공격할 적 구하기
    - 가장 가까운 & 가장 왼쪽
    - 좌상우 순서로 dfs진행
"""

import sys
from collections import deque
from copy import deepcopy
from itertools import combinations
input = sys.stdin.readline

def isFinished(b):
    for row in b:
        if sum(row) > 0:
            return False
    return True

# dfs
def attack_xy(ax, ay, b, d):
    visited = [[False] * len(b[0]) for _ in range(len(b))]
    dq = deque()
    dq.append((ax-1, ay, 1))
    visited[ax-1][ay] = True

    while dq:
        cx, cy, cd = dq.popleft()

        if b[cx][cy] == 1:
            return (cx, cy)
        
        for i in range(3):
            nx, ny = cx + dx[i], cy + dy[i]
            # 방문하지 않은 경우
            if 0 <= nx < len(b) and 0 <= ny < len(b[0]) and not visited[nx][ny] and cd+1 <= d:
                visited[nx][ny] = True
                dq.append((nx, ny, cd + 1))

    return None

def attack(rm, b):
    for x, y in rm:
        b[x][y] = 0
            
def play(a1, a2, a3, b, d):
    # 적이 모두 제거될 때까지 진행
    rm_cnt = 0
    # 적이 아닌 궁수가 이동!⭐️
    for ax in range(len(b), 0, -1):
        if isFinished(b):
            break
        # 궁수들 공격
        rm = set()
        rm.add(attack_xy(ax, a1, b, d))
        rm.add(attack_xy(ax, a2, b, d))
        rm.add(attack_xy(ax, a3, b, d))
        rm -= set([None])
        rm_cnt += len(rm)

        # 공격 처리
        attack(rm, b)
    return rm_cnt

n, m, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

# 좌상우로 이동
dx = [0, -1, 0]
dy = [-1, 0, 1]

# 궁수 배치 모든 경우의 수
archers = range(m)
for case in combinations(archers, 3):
    a1, a2, a3 = case
    tmp_board = deepcopy(board)
    answer = max(answer, play(a1, a2, a3, tmp_board, d))

print(answer)