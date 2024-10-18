# 연속 세 개의 구슬 색을 모두 다르게 하려고 한다.
# 백트래킹 + dfs

# 시간 초과
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
beadCntLsit = [int(input()) for _ in range(n)]
total = sum(beadCntLsit)

result = []
answer = 0

# N^35
def dfs(index):
    global answer
    if index >= total:
        answer += 1
        return

    for i in range(n):
        checkSet = set()
        if index >= 2:
            checkSet.add(result[index-1])
            checkSet.add(result[index-2])
        elif index == 1:
            checkSet.add(result[index-1])
        
        if i not in checkSet:
            if beadCntLsit[i] > 0:
                beadCntLsit[i] -= 1
                result.append(i)
                dfs(index + 1)
                result.pop()
                beadCntLsit[i] += 1
    
dfs(0)
print(answer)

# dfs + dp 신박한 풀이

n = int(input())
remains = [int(input()) for _ in range(n)]
dp = {}

def dfs(remains: list, a: int, b: int):

    state = (*remains, a, b)
    if state in dp:
        return dp[state]
    
    if sum(remains) == 0:
        return 1
    
    answer = 0
    for x in range(n):
        if remains[x] and x != a and x != b:
            remains[x] -= 1
            answer += dfs(remains, b, x)
            remains[x] += 1
        
    dp[state] = answer
    return answer

print(dfs(remains, -2, -1))