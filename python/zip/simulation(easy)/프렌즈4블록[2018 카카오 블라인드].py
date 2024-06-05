# 43분
def solution(m, n, board):
    nxtExist = True
    answer = 0
    # 매 단계에서 삭제될 수 있는 블록들 파악
    while nxtExist:
        # 삭제되는 블록이 있는지 확인 -> 있다면 다시 한 번 4블록 탐색해야 함
        nxtExist = False
        # 삭제할 블록 찾기
        tmprm = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != 0 and (board[i][j] == board[i+1][j] == board[i+1][j+1] == board[i][j+1]):
                    nxtExist = True
                    tmprm.add((i, j))
                    tmprm.add((i+1, j))
                    tmprm.add((i, j+1))
                    tmprm.add((i+1, j+1))
        
        # 블록 삭제 단계
        nBoard = []
        for i in range(n):
            tmpArr = []
            for j in range(m):
                if (j, i) not in tmprm: 
                    tmpArr.append(board[j][i])
            tmpArr = [0] * (m - len(tmpArr)) + tmpArr
            nBoard.append(tmpArr)
        board = list(map(list, zip(*nBoard[:])))
        answer += len(tmprm)
    
    return answer