# 시간 초과, 메모리 초과

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input())
names = set(input().split())

m = int(input())
des_cnt = defaultdict(int)
des_list = dict()
for name in names:
    des_list[name] = []

for _ in range(m):
    x, y = input().split()
    des_cnt[x] += 1
    des_list[y].append(x)

anc_cnt = names - set(des_cnt.keys())
print(len(anc_cnt))
print(*sorted(list(anc_cnt)))

des_level = defaultdict(int)
dq = deque()
for anc in anc_cnt:
    des_level[anc] = 1
    dq.append(anc)

while dq:
    cur = dq.popleft()

    for des in des_list[cur]:
        des_level[des] = des_level[cur] + 1
        dq.append(des)

for target in sorted(names):
    direct_des = []
    target_level = des_level[target]
    for des in des_list[target]:
        if des_level[des] == target_level + 1:
            direct_des.append(des)

    print(target, len(direct_des), *sorted(direct_des))

# 다른 풀이
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
people = set(input().split())
child = {person: [] for person in people}
edge = {person: [] for person in people}
indegree = {person:0 for person in people}
father = []

m = int(input())
for _ in range(m):
    a, b = input().split()
    indegree[a] += 1
    edge[b].append(a)

queue = deque()
for person in people:
    if indegree[person] == 0:
        queue.append(person)
        father.append(person)

while queue:
    node = queue.popleft()
    for nxt_node in edge[node]:
        indegree[nxt_node] -= 1
        if indegree[nxt_node] == 0:
            queue.append(nxt_node)
            child[node].append(nxt_node)

print(len(father))
print(*sorted(father))
for name in sorted(list(people)):
    print(name, len(child[name]), *sorted(child[name]))