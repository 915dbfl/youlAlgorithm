import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n, k = map(int, input().split())
heights = list(map(int, input().split()))

# 가림막 n-1개를 어디에 둬야 적절할까를 고민함 
# 이전값과 차이가 큰 쪽에 가림막을 두는 게 적절

# 1개의 조 예외 처리
if k == 1:
    print(heights[-1] - heights[0])
# 원생이 1명일 경우 예외 처리
elif n == 1:
    print(0)
else:
    hq = []
    for i in range(1, n):
        diff = heights[i] - heights[i-1]
        heappush(hq, [-diff, i])

    blind = []
    while k-1 > 0:
        cur = heappop(hq)
        blind.append(cur[1])
        k -= 1

    blind.sort()

    cost = 0
    blindIdx = 0
    Min = Max = 0
    for i in range(1, n):
        # 모든 가림막이 다 떨어졌을 때
        # heights 가장 마지막 원소와 현재 Min 차이 더하기
        if blindIdx >= len(blind):
            cost += heights[-1] - heights[Min]
            break

        # 해당 위치 다음에 가림막이 세워짐
        if blind[blindIdx] == i:
            # min과의 차이로 cost 계산
            cost += heights[Max] - heights[Min]
            # min과 max update
            Min = Max = i
            blindIdx += 1
        else:
            Max = i

    print(cost)

# 가림막을 세운다? = 해당 위치의 차이값은 더해지지 않는다.
# k-1개의 큰 차이를 제외하고 나머지를 더하면 값이 나온다.

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
heights = list(map(int, input().split()))

diff = []
for i in range(1, n):
    diff.append(heights[i] - heights[i-1])

diff.sort(reverse = True)
print(sum(diff[k-1:]))