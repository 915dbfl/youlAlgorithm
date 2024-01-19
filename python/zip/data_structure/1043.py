import sys
from collections import defaultdict,deque

n, m = map(int, sys.stdin.readline().split())
p = list(map(int, sys.stdin.readline().split()))
party = []
party_with = defaultdict(set)

truth = set(p[1:])
cnt = m

# 파티에 함께 참석하는 사람들 파악
for _ in range(m):
    tmp_set = set(list(map(int, sys.stdin.readline().split()))[1:])
    party.append(tmp_set)

    for i in tmp_set:
        party_with[i] |= tmp_set

# 진실을 아는 사람 파악
visited = [0] * (n+1)
dq = deque()

for i in truth:
    visited[i] = 1
    dq.append(i)

while dq:
    person = dq.popleft()

    for j in party_with[person]:
        if visited[j] == 0:
            dq.append(j)
            visited[j] = 1
            truth |= party_with[j]

# 과장을 할 수 있는 파티 수 계산
cnt = m
for case in party:
    if len(truth & case) > 0:
        cnt -= 1

print(cnt)

# 조금 더 간단한 풀이
# 1. truth, tmp_set 교집합이 하나라도 있으면 truth에 추가
# 2. 위 과정을 파티 수만큼 반복
    # 파티에서 진실을 알게 되는 새로운 사람이 생길 경우 처음 파티부터 다시 확인해야 함
    # 최악의 경우는 매 파티마다 진실을 알게 되는 새로운 사람이 생기는 것
    # 따라서 파티 수만큼 위의 과정을 반복

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
truth = set(input().split()[1:])
party = []

for _ in range(m):
    party.append(set(input().split()[1:]))

for _ in range(m):
    for p in party:
        if p & truth:
            truth |= p

cnt = 0
for p in party:
    if p & truth: # 진실을 아는 사람이 하나라도 있을 경우
        continue
    cnt += 1

print(cnt)