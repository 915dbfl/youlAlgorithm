# 1시간

def solution(board, skill):
    add = [[0] * len(board[0]) for _ in range(len(board))]
    
    # 누적합 설정
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1: # 공격
            degree *= -1
        
        add[r1][c1] += degree
        if r2+1 < len(board):
            add[r2+1][c1] -= degree
        if c2+1 < len(board[0]):
            add[r1][c2+1] -= degree
        if r2+1 < len(board) and c2+1 < len(board[0]):
            add[r2+1][c2+1] += degree
            
    # 누적합 계산
    for j in range(1, len(board[0])):
        add[0][j] += add[0][j-1]
        
    for i in range(1, len(board)):
        add[i][0] += add[i-1][0]
        
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            add[i][j] += add[i-1][j] + add[i][j-1] - add[i-1][j-1]
            
    # 결과 계산
    answer = len(board) * len(board[0])
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + add[i][j] <= 0:
                answer -= 1
    return answer