# 위상 정렬
# 15분

"""
1. m의 순서 반복
    1) 위상을 저장한다.
    2) m 다음에 오는 문제를 리스트로 저장한다.
2. 위상이 0인 것을 뽑고, 숫자 순으로 정렬한다.
3. while문을 통해 heapq 길이가 0이 될 때까지 진행한다.
    1) 이때 문제 번호 가 가장 작은 것을 pop하게 한다.
"""
import sys
input = sys.stdin.readline

from collections import defaultdict
from heapq import heappush, heappop

n, m = map(int, input().split())
degree = [0] * (n+1)
childs = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    degree[b] += 1
    childs[a].append(b)

hq = []
for i in range(1, n+1):
    if degree[i] == 0:
        heappush(hq, i)

order = []
while hq:
    cur = heappop(hq)
    order.append(cur)

    for nxt in childs[cur]:
        degree[nxt] -= 1
        if degree[nxt] == 0:
            heappush(hq, nxt)

print(*order)