# 실패

import sys
input = sys.stdin.readline

answer = []

for _ in range(4):
    case = list(map(int, input().split()))
    win = 0
    draw = []
    lose = 0

    for i in range(0, len(case), 3):
        if case[i] + case[i+1] + case[i+2] != 5:
            answer.append("0")
            break
        
        # 승의 결과
        for j in range(3):
            if (i+j) % 3 == 0:
                win += case[i+j]
            elif (i+j) % 3 == 1:
                if case[i+j] > 0:
                    draw.append(case[i+j])
            else:
                lose += case[i+j]


    if (win != lose) or len(draw) % 2 != 0 or sum(draw) % 2 != 0:
        answer.append("0")
    else:
        answer.append("1")

print(" ".join(answer))

# 백트래킹
# 시간 복잡도: O(3**15)

import sys
from itertools import combinations
input = sys.stdin.readline

def dfs(depth):
    global cnt

    # 15번째 경기에 도달했을 때
    if depth == 15:
        cnt = 1
        # 모든 score가 0인지 확인
        for sub in res:
            if sub.count(0) != 3:
                cnt = 0
                break
        return
    
    # game[depth] 경기
    g1, g2 = game[depth]
    # game[depth] 경기에서 가능한 승부 확인
    for x, y in ((0, 2), (1, 1), (2, 0)):
        if res[g1][x] and res[g2][y] > 0:
            res[g1][x] -= 1
            res[g2][y] -= 1
            dfs(depth + 1)
            # 백트래킹 진행
            res[g1][x] += 1
            res[g2][y] += 1

game = list(combinations(range(6), 2))
answer = []

for _ in range(4):
    score = list(map(int, input().split()))
    res = [score[i:i+3] for i in range(0, len(score)-1, 3)]
    cnt = 0
    dfs(0)
    answer.append(cnt)

print(*answer)