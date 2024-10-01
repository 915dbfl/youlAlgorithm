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

case = list(combinations(range(6), 2))
state = [(2, 0), (1, 1), (0, 2)]
caseResult = 0
answer = []

def dfs(matchTime):
    global caseResult
    if matchTime > 14:
        if sum(map(sum, resultByUser)) == 0:
            caseResult = 1
        return

    p1, p2 = case[matchTime]
    for (s1, s2) in state:
        if resultByUser[p1][s1] > 0 and resultByUser[p2][s2] > 0:
            resultByUser[p1][s1] -= 1
            resultByUser[p2][s2] -= 1
            dfs(matchTime+1)
            resultByUser[p1][s1] += 1
            resultByUser[p2][s2] += 1

for _ in range(4):
    result = list(map(int, input().split()))
    resultByUser = [result[i:i+3] for i in range(0, len(result), 3)]
    caseResult = 0
    dfs(0)
    answer.append(caseResult)

print(*answer)