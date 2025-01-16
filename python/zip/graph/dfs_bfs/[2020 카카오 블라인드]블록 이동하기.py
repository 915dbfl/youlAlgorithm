# 1시간 반
# 회고: 중간중간 변수명 틀린 것은 없나 확인하기,,

"""
[풀이과정]
1. 로봇 위치 중 하나를 중심으로 이동
2. 다른 위치 하나는 dir로 저장해둠
3. 1번 위치를 중심으로 상하좌우 이동
4. 각 위치에서 [0, 0, 0, 0]으로 중복 방문 제어
"""

from collections import deque
import sys

# 상, 우, 하, 좌 순서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
    
def is_finished(n, curx, cury, pair_dir):
    pairx = curx + dx[pair_dir]
    pairy = cury + dy[pair_dir]
    
    # 로봇의 어느 한쪽이라도 끝에 도달한 경우
    if (curx == n-1 and cury == n-1) or (pairx == n-1 and pairy == n-1):
        return True
    return False

def can_go(n, x, y, board):
    return 0<=x<n and 0<=y<n and board[x][y] == 0

def check_visited(x, y, px, py, dir, visited):
    # 방문을 하지 않았다면
    if not visited[x][y][dir] and not visited[px][py][(dir+2)%4]:
        visited[x][y][dir] = True
        visited[px][py][(dir+2)%4] = True
        return True
    return False

def solution(board):
    n = len(board)
    visited = [[[False, False, False, False] for _ in range(n)] for _ in range(n)]
    visited[0][0][1] = True
    visited[0][1][3] = True

    dq = deque()
    dq.append((0, 1, 3, 0))
    
    while dq:
        curx, cury, pair_dir, curm = dq.popleft()
        
        if is_finished(n, curx, cury, pair_dir):
            return curm
        
        # 이동 시작
        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]
            pairx = nx + dx[pair_dir]
            pairy = ny + dy[pair_dir]
            
            # 갈 수 있을 경우
            if can_go(n, nx, ny, board) and can_go(n, pairx, pairy, board):
                # 방문했던 곳이 아닌지 확인
                if check_visited(nx, ny, pairx, pairy, pair_dir, visited):
                    dq.append((nx, ny, pair_dir, curm + 1))
    
        # 회전이 가능할 경우 회전 시작
        # 단, 회전은 아무 축이나 가능하다.
        for bx, by, pdir in [[curx, cury, pair_dir], [curx + dx[pair_dir], cury + dy[pair_dir], (pair_dir + 2) % 4]]:
            for i in range(1, 4):
                ndir = (pdir + i) % 4
                nmove = ((i + 1) % 2) + 1
                
                # 회전할 때 확인해야 하는 대각선
                chx = bx + dx[pdir] + dx[ndir]
                chy = by + dy[pdir] + dy[ndir]
                # 회전 후 위치
                npx = bx + dx[ndir]
                npy = by + dy[ndir]
                

                # 이동할 수 있다면
                if can_go(n, chx, chy, board) and can_go(n, npx, npy, board):
                    # 방문했던 곳인지 확인
                    if check_visited(bx, by, npx, npy, ndir, visited):
                        dq.append((bx, by, ndir, curm + nmove))

# 간단한 풀이법
from collections import deque

def solution(board):
    n = len(board)
    # 하우상좌
    dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    
    # (행, 열, 로봇이 놓인 방향, 이동 횟수)
    # 방향: 가로(0), 세로(1)
    dq = deque([(0, 0, 1, 0)])
    visited = set([0, 0, 1])
    
    while dq:
        r1, c1, d, mv = dq.popleft()
        r2, c2 = r1 + dir[d][0], c1 + dir[d][1]
        
        # 목적지 도착 확인
        if r2 == n-1 and c2 == n-1:
            return mv
        
        # 하우상좌로 이동
        for i in range(4):
            nr1, nc1 = r1 + dir[i][0], c1 + dir[i][1]
            nr2, nc2 = r2 + dir[i][0], c2 + dir[i][1]
            
            # 보드를 벗어나지 않은 범위로만 이동
            if 0<=nr1<n and 0<=nc1<n and 0<=nr2<n and 0<=nc2<n:
                # 이미 방문 or 벽이 있는 경우 제외
                if (nr1, nc1, d) in visited or board[nr1][nc1] == 1 or board[nr2][nc2] == 1:
                    continue
                    
                # 현재 방향을 유지한채로 상하좌우로 이동
                dq.append((nr1, nc1, d, mv + 1))
                visited.add((nr1, nc1, d))
                
                # 회전
                nd = d ^ 1
                # 로봇 세로 + 오른쪽 회전 / 로봇 가로 + 아래쪽 회전
                if i + d == 1:
                    if (r1, c1, nd) not in visited:
                        dq.append((r1, c1, nd, mv+1))
                        visited.add((r1, c1, nd))
                    if (r2, c2, nd) not in visited:
                        dq.append((r2, c2, nd, mv+1))
                        visited.add((r2, c2, nd))
                # 로봇 가로 + 위쪽 회전 / 로봇 세로 + 왼쪽 회전
                elif i + d == 3:
                    if (nr1, nc1, nd) not in visited:
                        dq.append((nr1, nc1, nd, mv+1))
                        visited.add((nr1, nc1, nd))
                    if (nr2, nc2, nd) not in visited:
                        dq.append((nr2, nc2, nd, mv+1))
                        visited.add((nr2, nc2, nd))