#22.02.08
#크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    size = len(board)
    backet = []
    
    for i in moves:
        for j in range(size):
            tmp = board[j][i-1]
            if tmp != 0:
                if len(backet) != 0 and backet[-1] == tmp:
                    answer += 2
                    backet.pop()
                else: 
                    backet.append(tmp)
                board[j][i-1] = 0
                break
            
    return answer