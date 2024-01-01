#드래곤 앤 던전

# 단순 구현: 누적합, dp
# n값이 작으므로 이분탐색으로 찾을 필요 없음
import sys
from math import ceil

n, mAtk = map(int, input().split())
result = 0
dp = [0] * (n+1)

for i in range(1, n+1):
    t, a, h = map(int, sys.stdin.readline().split())
    if t == 1:
        tmp = ceil(h/mAtk) - 1
        dp[i] = dp[i-1] + tmp * a
    else:
        mAtk += a
        dp[i] = max(0, dp[i-1] - h)
 
print(max(dp)+1)

# 이분 탐색
import sys
from math import ceil 

n, mAtk = map(int, input().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
left, right, answer = 0, sys.maxsize, 0

def binarySearch(atk, curHp, maxHp):
    for t, a, h in room:
        if t == 1:
            tmp = ceil(h/atk) - 1
            curHp -= tmp * a
        else:
            atk += a
            curHp = min(maxHp, curHp + h)

        if curHp <= 0:
            return False
    return True            

while left <= right:
    mid = (left + right)//2
    if binarySearch(mAtk, mid, mid):
        right = mid - 1
        answer = mid
    else:
        left = mid + 1

print(answer)