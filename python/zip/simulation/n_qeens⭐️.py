# 브루트 포스, 백트레킹
# 과정
# 1. 0부터 차례대로 증가하며 해당 행 어떤 열에 값을 넣을지 결정
# 2. 해당 행, 열에 퀸을 위치시킬 경우 확인해야 할 점
# 2-1. 해당 열에 있는 퀸이 있는지
# 2-2. 대각선에 퀸이 있는지
def solution(n):
    row = [0] * n
    answer = 0
    
    def is_promising(x):
        # 해당 행 이전 행들만 확인하면 된다.
        for i in range(x):
            # 동일한 열이 있는지, 대각선인 퀸이 있는지 확인
            if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
                return False
        return True
    
    # 재귀 진행
    def n_queens(x):
        nonlocal answer
        # n행까지 모두 진행한 경우
        if x == n:
            answer += 1
            return
        
        # 0 - n-1열까지 모두 확인
        for i in range(n):
            row[x] = i # x, i에 퀸을 놀 경우
            if is_promising(x):
                n_queens(x+1)
                
    n_queens(0)
    return answer