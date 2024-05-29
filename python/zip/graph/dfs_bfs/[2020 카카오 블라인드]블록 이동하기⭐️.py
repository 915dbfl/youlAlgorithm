from collections import deque

def solution(board):
    n = len(board)
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
        
        # 상하좌우로 이동
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