# 오답 / 재풀이 필요

import sys
from collections import defaultdict, deque

answer = sys.maxsize
card_dict = defaultdict(list)
remove_num = [False] * 6

def is_game_finished(board):
    for line in board:
        if sum(line) != 0:
            return False
    return True

def get_min_dist(x1, y1, x2, y2, board):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    dq = deque()
    dq.append((x1, y1))
    visited = [[sys.maxsize for _ in range(4)] for _ in range(4)]
    visited[x1][y1] = 0
    
    while dq:
        curx, cury = dq.popleft()
        if curx == x2 and cury == y2:
            return visited[curx][cury]
        
        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]
            
            if 0<=nx<4 and 0<=ny<4 and visited[nx][ny] > visited[curx][cury] + 1:
                visited[nx][ny] = visited[curx][cury] + 1
                dq.append((nx, ny))
        
        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]
            while 0<=nx + dx[i]<4 and 0<=ny + dy[i]<4 and board[nx][ny] == 0:
                nx = nx + dx[i]
                ny = ny + dy[i]
            if 0<=nx<4 and 0<=ny<4 and visited[nx][ny] > visited[curx][cury] + 1:
                visited[nx][ny] = visited[curx][cury] + 1
                dq.append((nx, ny))
                
    
def dfs(curx, cury, curm, board):
    global answer
    # 게임이 끝난 경우
    if is_game_finished(board):
        answer = min(answer, curm)
        return
    
    for key in card_dict.keys():
        if remove_num[key]: continue
        
        card1, card2 = card_dict[key]
        to_start = get_min_dist(curx, cury, *card1, board)
        to_end = get_min_dist(curx, cury, *card2, board)
        min_dist = get_min_dist(*card1, *card2, board)

        board[card1[0]][card1[1]] = 0
        board[card2[0]][card2[1]] = 0
        remove_num[key] = True
        
        dfs(card1[0], card1[1], curm + to_end + min_dist + 2, board)
        dfs(card2[0], card2[1], curm + to_start + min_dist + 2, board)

        board[card1[0]][card1[1]] = key
        board[card2[0]][card2[1]] = key
        remove_num[key] = False
        

def solution(board, r, c):
    global answer
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                card_dict[board[i][j]].append((i, j))
            
    dfs(r, c, 0, board)
    return answer