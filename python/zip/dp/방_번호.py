# dp
# 이전에 모든 값 확인하는 로직 추가해야 함!
# 반례:
# 5
# 1 2 3 4 5
# 15

import sys
input = sys.stdin.readline

def checkBigger(base, target):
    if base == "" or target == "":
        if base == "":
            return True
        else:
            return False
    return int(base) < int(target)

def makeNewNum(base, new):
    if base == "" or new == "":
        if base == "":
            return new
        else:
            return base
        
    tmp = list(base) + list(new)
    tmp.sort(reverse = True)

    return "".join(tmp)
  
n = int(input())
costs = list(map(int, input().split()))
m = int(input())

# 초기값 채우기
# 동일한 값이더라도 나중에 입력되는 값이 더 높은 수
dp = [""] * 51
for i in range(n):
    dp[costs[i]] = str(i)

for i in range(1, m+1):
    if checkBigger(dp[i], dp[i-1]):
        dp[i] = dp[i-1]
    
    # 이전 모든 값 확인하기
    # j + (i-j)으로 살 수 있는 최대 방번호 구하기
    for j in range(i-1, -1, -1):
        new = makeNewNum(dp[j], dp[i-j])
        if checkBigger(dp[i], new):
            dp[i] = new

    # 모든 숫자 확인하기
    # j번째 숫자를 추가할 경우
    for j in range(n):
        if i-costs[j] >=0:
            new = makeNewNum(dp[i-costs[j]], str(j))
            if checkBigger(dp[i], new):
                dp[i] = new

print(dp[m])

# 충격적으로 짧은 dp 풀이..
import sys
input = sys.stdin.readline

n = int(input())
costs = list(map(int, input().split()))
m = int(input())

dp = [-1] * (m+1)

# 큰 숫자부터 확인
# 큰 숫자를 살 수 있으면 사라!
# dp[cost]를 증가하면서 업데이트가 반영되도록 한다.
for i in range(n-1, -1, -1):
    cost = costs[i]

    # x원 빝으로는 살 수가 없으므로 x - m원 조사
    for j in range(cost, m+1):
        dp[j] = max(dp[j], i, dp[j-cost]*10 + i)

print(dp[m])