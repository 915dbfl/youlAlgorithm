# 1시간 40분

"""
주요 정보
1. 3*3 보드판
2. 같은 글자를 가로 / 세로 / 대각선으로 놓이면 승리
3. 항상 각 선수는 최적의 플레이를 한다.

풀이 과정
1. turn을 계산한다.
    1과 2의 개수 중에서 더 적은 개수 / 동일하다면 1이 turn
2. 1 / 2 착수 진행 - 재귀 
    - 최적의 플레이를 한다?
        다음 플레이어가 패배 > 무습부 > 승이 될 수 있도록 플레이
"""

import sys
input = sys.stdin.readline

def play(turn):
    global answer

    if isFinished(turn):
        return 0
    
    # 적: 패배 > 무승부 > 승 순으로 선택
    min_result = 3
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = turn
                min_result = min(min_result, play((turn % 2) + 1))
                board[i][j] = 0

    if min_result == 2:
        return 0
    elif min_result == 1 or min_result == 3:
        return 1
    else:
        return 2

def isFinished(turn):
    bf_turn = (turn%2) + 1
    # 대각선 확인
    if board[0][0] == board[1][1] == board[2][2] == bf_turn:
        return True
    elif board[0][2] == board[1][1] == board[2][0] == bf_turn:
        return True

    # 가로 / 세로 확인
    for i in range(3):
        if (board[0][i] == board[1][i] == board[2][i] == bf_turn) or (board[i][0] == board[i][1] == board[i][2] == bf_turn):
            return True

    return False

board = [list(map(int, input().split())) for _ in range(3)]
resultDict = {0: 'L', 1: 'D', 2: 'W'}
answer = 0
cnt = [0, 0, 0]
for i in range(3):
    for j in range(3):
        cnt[board[i][j]] += 1

# 이미 무승부라면
if cnt[0] == 0:
    print('D')
else:
    # 착수 플레이어 계산
    turn = 1 if cnt[1] == cnt[2] else 2
    target = turn

    print(resultDict[play(turn)])