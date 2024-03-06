# 단순 스택을 pop하는 방식으로 풀었을 때 반례
# 1 1 2 5 6 7 7 6 5 5 5 2

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dq = deque([nums[0]])
candidate = deque()
answer = 0
for i in range(1, n):
    if len(dq) > 0 and dq[-1] == nums[i]:
        dq.pop()
        if len(dq) == 0:
            answer += 1
            if len(candidate) > 0:
                candidate.clear()
        else:
            candidate.append(nums[i])
    else:
        if len(candidate) > 0:
            tmpDq = deque()
            for cd in candidate:
                tmpDq.append(cd)
                tmpDq.appendleft(cd)
            
            for cd in tmpDq:
                dq.append(cd)

            candidate.clear()
        dq.append(nums[i])

if len(dq) == 0 and answer != 0:
    print(answer)
else:
    print(-1)

# 다른 풀이
# O(n^2)
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

def solve():
    result, x = 0, 0

    # 짝수 팰린드롬이므로 y를 2씩 증가시킴
    # 2씩 "증가"시키므로 팰린드롬의 최대 수를 구할 수 있음
    for y in range(1, n, 2):
        if nums[x] != nums[y]:
            continue

        check = True

        # x~y의 중간값까지만 팰린드롬인지 확인
        for diff in range(1, (y-x-1)//2 + 1):
            if nums[x+diff] != nums[y-diff]:
                check = False
                break

        if check:
            result += 1
            x = y + 1

    # 팰린드롬이 만들어지지 않는다면
    if x != n:
        return -1

    return result

answer = solve()
print(answer if answer != 0 else -1)

# dp 활용하기
# 1. 이중 for문을 활용해 배열의 팰린드롬 상태 저장
# 2. 2씩 증가시키며 가장 먼저 n에 도달했을 때 result 출력

import sys
input = sys.stdin.readline

def check(cur, cnt):
    global answer
    if cur == n:
        print(cnt)
        exit()
    
    for nxt in range(cur+1, n, 2):
        if dp[cur][nxt]:
            check(nxt+1, cnt+1)

n = int(input())
arr = list(map(int, input().split()))

dp = [[True if i == j else False for i in range(n)] for j in range(n)]

# 2개짜리 팰린드롬 확인
for i in range(n-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = True

# 모든 팰린드롬 확인
for i in range(2, n):
    for j in range(n-i):
        if arr[j] == arr[j+i] and dp[j+1][j+i-1]:
            dp[j][j+i] = True

check(0, 0)
print(-1)