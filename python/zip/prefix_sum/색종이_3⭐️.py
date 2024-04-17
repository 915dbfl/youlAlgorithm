# 누적합
# 비슷한 문제: 히스토그램
import sys
input = sys.stdin.readline

n = int(input())
board = [[0 for _ in range(110)] for _ in range(110)]

# 위치 찍어놓기
for _ in range(n):
    a, b = map(int, input().split())

    # 색종이가 있는 위치를 모두 1로 표시
    # 색종이의 개수 100 이하, 10*10인 사격형이므로 충분히 가능하다.
    for i in range(a, a+10):
        for j in range(b, b+10):
            board[i][j] = 1

# 세로로 누적합 구하기
# -> 각 지점의 값이 각 지점의 세로 높이와 같아진다.
for i in range(99):
    for j in range(100):
        if board[i][j] != 0 and board[i+1][j] != 0:
            board[i+1][j] = board[i][j] + 1

# i, j 위치에서 오른쪽으로 가능한 최대 사각형 넓이를 구하는 과정
# O(n**3) = O(10^6)
answer = 0
for i in range(100):
    for j in range(100):
        h = 100
        # 현재 위치를 기준으로 오른쪽만 보면서 가능한 높이를 구하고
        # 구한 높이를 통해 사각형의 넓이를 구한다
        for k in range(j, 100):
            h = min(h, board[i][k])
            if h == 0:
                break
            # 사각형 넓이 구하기
            answer = max(answer, h*(k-j+1))
                         
print(answer)