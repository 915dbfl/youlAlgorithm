# 재풀이 (40분)
"""
패배하는 경우
1. 움직일 차례인데 주변 4칸에 모두 발판이 없는 경우
2. 두 캐릭터가 같은 발판 위에 존재 -> 다른 발판으로 이동 시 상대 캐릭터 패배

재귀 (승리 여부, 이동 횟수 반환)
1. 이동할 곳이 없다면 -> (false, 0)
2. 같은 발판 -> (true, 1)
3. 4군데로 이동
"""

import sys

def solution(board, aloc, bloc):
    n = len(board)
    m = len(board[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def is_valid(curx, cury, board):
        return 0 <= curx < n and 0 <= cury < m and board[curx][cury] == 1
    
    def can_move(curx, cury, board):
        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]
            
            # 범위 내이고, 발판이 있을 경우
            if is_valid(nx, ny, board):
                return True
        return False
                
    def play(curx, cury, otherx, othery, board):
        # 이동할 수 없는 경우
        if not can_move(curx, cury, board):
            return [False, 0]
        
        # 동일한 위치에 있을 경우 -> 한 번 이동 후 승리
        if curx == otherx and cury == othery:
            return [True, 1]
        
        lose_max = -1
        win_min = sys.maxsize
        
        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]
            
            if is_valid(nx, ny, board):
                board[curx][cury] = 0
                result = play(otherx, othery, nx, ny, board)
                # 상대방이 이기는 경우
                if result[0]:
                    lose_max = max(lose_max, result[1] + 1)
                # 상대방이 지는 경우
                else:
                    win_min = min(win_min, result[1] + 1)
                board[curx][cury] = 1
                
        # 이길 방법이 있다면?
        if win_min != sys.maxsize:
            return [True, win_min]
        else:
            return [False, lose_max]
    
    result = play(aloc[0], aloc[1], bloc[0], bloc[1], board)
    return result[1]
    
# dfs
import sys
sys.setrecursionlimit(10**6)

def solution(board, aloc, bloc):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def in_range(x, y):
        if 0 <= x < len(board) and 0 <= y < len(board[0]):
            return True
        return False
    
    def is_finished(x, y):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if in_range(nx, ny) and board[nx][ny]:
                return False
        return True
    
    def dfs(x1, y1, x2, y2):
        # 이동이 불가할 경우
        if is_finished(x1, y1):
            return [False, 0]
        
        # 서로 동일한 위치에 있을 경우
        # 해당 플레이어가 움직일 때 다른 플레이어는 바로 패배
        if x1 == x2 and y1 == y2:
            return [True, 1]
        
        min_move = sys.maxsize
        max_move = 0
        can_win = False
        
        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            
            if in_range(nx, ny) and board[nx][ny]:
                board[x1][y1] = 0
                result = dfs(x2, y2, nx, ny)
                board[x1][y1] = 1
                
                if not result[0]: # 항상 이기는 경우
                    min_move = min(min_move, result[1])
                    can_win = True
                else:
                    max_move = max(max_move, result[1])
        
        # 이길 수 있다면
        if can_win:
            return [True, min_move + 1]
        else:
            return [False, max_move + 1]
            
    return dfs(*aloc, *bloc)[1]

# 나의 풀이: 오답
# 최적의 플레이가 무엇인지를 제대로 이해하지 않음

from collections import deque

def solution(board, aloc, bloc):
    answer = [len(board) * len(board[0]), 0]
    
    # 이동을 위한 배열
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def update_answer(amove, bmove):
        nonlocal answer
        if amove < answer[0]:
            answer = [amove, bmove]
        elif amove == answer[0] and bmove > answer[1]:
            answer = [amove, bmove]

    # a의 위치, b의 위치, 차례, 사라진 발판 정보
    def dfs(aloc, bloc, amove, bmove, turn):
        curx, cury = aloc if not turn else bloc
        
        # 서있는데 발판이 사라진 경우 체크
        if not board[curx][cury]:
            update_answer(amove, bmove)
            return
        
        move = False # 이동 여부
        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]
        
            # board 범위 내인지 파악
            if 0<=nx<len(board) and 0<=ny<len(board[0]):
                # 발판이 존재하는지 
                if board[nx][ny]:
                    move = True # 이동 체크
                    board[curx][cury] = 0 # 발판 제거
                    if not turn:
                        dfs([nx, ny], bloc, amove + 1, bmove,  1)
                    else:
                        dfs(aloc, [nx, ny], amove, bmove + 1, 0)
                    board[curx][cury] = 1 # 백트래킹 : 발판 복구
                    
        if not move: # 이동할 수가 없는 경우
            update_answer(amove, bmove)
            
    dfs(aloc, bloc, 0, 0, 0)
    return sum(answer)