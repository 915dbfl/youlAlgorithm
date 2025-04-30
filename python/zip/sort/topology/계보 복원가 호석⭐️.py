# 계보 복원가 호석

"""
# 풀이과정 (위상 정렬)
1. 차수 기록 -> 시조 구분 / 위상 정렬을 위해
2. deque 사용
    - 시조 기록
    - 차수가 0이 될 경우 -> 해당 node가 부모가 됨
"""

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
people = list(input().split())
degree = {person: 0 for person in people}
edge = {person: [] for person in people}
child = {person: [] for person in people}

m = int(input())
for _ in range(m):
    ch, p = input().split()
    degree[ch] += 1
    edge[p].append(ch)

ancestor = []
dq = deque()
for person in people:
    if degree[person] == 0:
        ancestor.append(person)
        dq.append(person)

while dq:
    cur = dq.popleft()

    for ch in edge[cur]:
        degree[ch] -= 1
        if degree[ch] == 0:
            dq.append(ch)
            child[cur].append(ch)

print(len(ancestor))
print(*sorted(ancestor))
for person in sorted(people):
    print(person, len(child[person]), *sorted(child[person]))