# 맥주 축제

# bfs: 메모리 초과
import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
beers = []
for _ in range(k):
    v, c = map(int, sys.stdin.readline().split())
    beers.append((v, c))

beers.sort(key = lambda x:x[1])

def bfs():
    dq = deque()
    dq.append((0, -1, 0)) # 선호도 합, cur, time

    while dq:
        pref, cur, time = dq.popleft()
        
        if time == n:
            if pref >= m:
                print(beers[cur][1])
                break
        
        for i in range(cur+1, len(beers)):
            dq.append((pref + beers[i][0], i, time+1))

    print(-1)

bfs()
        
# 우선순위 큐
# 그리디
# (도수 낮은 순, 선호도 높은 순)으로 정렬
# 도수가 낮은 순으로 마신다.
# 마신 맥주의 수가 n이 된다면 선호도를 확인한다.
    # 선호도가 m 이상이라면 가장 최근에 마신 맥주(도수가 가장 높은 맥주)의 값을 출력한다.
    # 선호도가 m 이하라면 우선순위 큐에서 선호도가 가장 작은 값을 제외한다.⭐️
    # 여기서 가장 최근에 마신 맥주가 아닌 선호도가 가장 작은 값을 제외한다.
    # 가장 최근에 마신 맥주를 제외할 경우, 어차피 선호도를 채우기 위해 도수가 더 높은 다음 맥주를 마셔야 한다.
    # 하지만 선호도가 가장 작은 값을 제외한다. 도수가 더 높은 다음 맥주를 마시지만 채워야하는 선호도가 적어지게 된다.
import sys
import heapq

n, m, k = map(int, sys.stdin.readline().split())

beers = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
beers.sort(key = lambda x: (x[1], -x[0]))

pref = 0
hq = []

for b in beers:
    pref += b[0]
    heapq.heappush(hq, b[0])

    if len(hq) == n:
        if pref >= m:
            answer = b[1]
            break
        else:
            pref -= heapq.heappop(hq)
else:
    print(-1)
    exit()

print(answer)

# 이분탐색
# 도수 레벨에서 이분탐색을 진행한다.
    # 해당 도수의 레벨 이하의 맥주가 n개 이상이고, n개까지 선호도의 총합이 m 이상인지를 체크한다.
    # n개까지 선호도의 총합을 확인할 수 있는 이유는 선호도 순으로 정렬되어 있기 때문이다.

import sys


def check(val):
    temp = [i[0] for i in arr if i[1] <= val]
    return N <= len(temp) and M <= sum(temp[:N])


def binary_search(left, right):
    ans = -1
    arr.sort(key=lambda x: -x[0])
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans


N, M, K = map(int, sys.stdin.readline().rstrip().split())
arr = []
for i in range(K):
    v, c = map(int, sys.stdin.readline().rstrip().split())
    arr.append((v, c))

arr.sort(key=lambda x: x[1])

print(binary_search(arr[0][1], arr[-1][1]))  