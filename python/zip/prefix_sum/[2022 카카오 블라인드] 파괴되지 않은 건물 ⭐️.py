def solution(board, skill):
    # 누적합
    row = len(board)
    col = len(board[0])
    pf = [[0] * col for _ in range(row)]
    
    # sikill의 최대 수 * r2-r1의 최대 크기 = 250000 * 1000 (시간 초과)
    for type, r1, c1, r2, c2, degree in skill:
        degree = -degree if type == 1 else degree
        # 누적합 업데이트
        for x in range(r1, r2+1):
            # degree +
            pf[x][c1] += degree
            # 더한 degree 원상복구
            if c2+1 >= col:
                if x+1 < row:
                    pf[x+1][0] += -degree
            else:
                pf[x][c2+1] += -degree
                
    answer = row * col
    tmp = 0
    for i in range(row):
        for j in range(col):
            tmp += pf[i][j]
            board[i][j] += tmp
            if board[i][j] <= 0:
                answer -= 1
    return answer

# 2차원 배열 누적합⭐️
def solution(board, skill):
    # 누적합
    row = len(board)
    col = len(board[0])
    pf = [[0] * col for _ in range(row)]
    tmp = 0
    for type, r1, c1, r2, c2, degree in skill:
        degree = -degree if type == 1 else degree
        pf[r1][c1] += degree
        if c2+1 < col:
            pf[r1][c2+1] -= degree
        if r2+1 < row:
            pf[r2+1][c1] -= degree
        if c2+1 < col and r2+1 < row:
            pf[r2+1][c2+1] += degree
            
    for i in range(row):
        for j in range(1, col):
            pf[i][j] += pf[i][j-1]
    
    for j in range(col):
        for i in range(1, row):
            pf[i][j] += pf[i-1][j]
    
    answer = row * col
    for i in range(row):
        for j in range(col):
            if board[i][j] + pf[i][j] <= 0:
                answer -= 1
    return answer