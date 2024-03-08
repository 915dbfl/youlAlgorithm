# 모든 경우를 확인해야 함 -> 3^100 시간 복잡도 초과
# dfs
# 부분 성공
import sys
from collections import deque
input = sys.stdin.readline

def dfs():
    dq = deque()
    dq.append((0, 0, 0)) # cur, cost, amount of coupon
    answer = 37000*n

    while dq:
        cur, cost, coupon = dq.popleft()

        if cost > answer:
            continue

        if cur >= n:
            answer = min(answer, cost)
            continue

        # 현재 방법이 이전 방법보다 저렴한 경우
        # 머물지 않는 경우
        if notStay[cur] == 1:
            dq.append((cur+1, cost, coupon))

        else:
            # 하루권 구매
            # 사용할 쿠폰이 있는 경우
            if coupon >= 3:
                dq.append((cur+1, cost, coupon-3))
            # 쿠폰을 사용하지 않고 하루권을 구매하는 경우
            else:
                dq.append((cur+1, cost+10000, coupon))

            # 3일권 구매
            if cur <= n-3:
                dq.append((cur+3, cost+25000, coupon+1))
            
            # 5일권 구매
            if cur <= n-5:
                dq.append((cur+5, cost+37000, coupon+2))

    print(answer)
                

n, m = map(int, input().split())

notStay = [0 for _ in range(n)]
if m > 0:
    for i in list(map(int, input().split())):
        notStay[i-1] = 1

dfs()

# dp
# dp[day][coupon]: 해당 날짜에 해당 쿠폰 개수를 가지고 있을 때 최소 비용

import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
noStay = set(map(int, input().split()))

dp = [[INF] * 41 for _ in range(n+1)]
dp[0][0] = 0

for i in range(n+1):
    for j in range(40):
        # 해당 날짜에 해당 쿠폰 개수로 도달할 수 없는 경우
        if dp[i][j] == INF:
            continue
        result = dp[i][j]

        # 머무는 날이 아닌 경우
        if i+1 <= n and i+1 in noStay:
            dp[i+1][j] = min(result, dp[i+1][j])
        
        # 쿠폰을 쓸 수 있는 경우
        if i+1 <= n:
            if j >= 3:
                dp[i+1][j-3] = min(result, dp[i+1][j-3])

            # 1일권 구매
            dp[i+1][j] = min(result + 10000, dp[i+1][j])

        # 3일권 구매
        for k in range(1, 4):
            if i+k <= n and j+1 <= 40:
                dp[i+k][j+1] = min(result + 25000, dp[i+k][j+1])
        # 5일권 구매
        for k in range(1, 6):
            if i+k <= n and j+2 <= 40:
                dp[i+k][j+2] = min(result + 37000, dp[i+k][j+2])

print(min(dp[-1]))

# dfs + 탑다운 dp
import sys
input = sys.stdin.readline
COST1, COST2, COST3 = 10000, 25000, 37000

def dfs(date, coupon):
    if date > n: return 0

    if dp[date][coupon] != -1:
        return dp[date][coupon]
    
    # 머물지 않는 날이라면
    if date in noStay:
        dp[date][coupon] = dfs(date+1, coupon)
        return dp[date][coupon]
    
    dp[date][coupon] = min(
        dfs(date+1, coupon) + COST1,
        dfs(date+3, coupon+1) + COST2,
        dfs(date+5, coupon+2) + COST3
    )

    if coupon >= 3:
        dp[date][coupon] = min(dp[date][coupon], dfs(date+1, coupon-3))

    return dp[date][coupon]

n, m = map(int, input().split())
noStay = []
if m > 0:
    noStay = set(map(int, input().split()))

dp = [[-1]*40 for _ in range(n+6)]
print(dfs(1, 0))