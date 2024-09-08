# union find
# 34분, 오답
# 접근 방법은 맞는데 왜 오답인지 모르겠음

import sys
from collections import Counter
input = sys.stdin.readline

def findParent(a):
    if parent[a] != a:
        parent[a] = findParent(parent[a])
    return parent[a]
    
def union(a, b):
    a = findParent(a)
    b = findParent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def createUnion(i):
    for nxt in graph[i]:
        if findParent(i) != findParent(nxt):
            union(i, nxt)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
parent = [i for i in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

c, h, k = map(int, input().split())

# 모든 동맹국 구하기
for i in range(1, n+1):
    if parent[i] == i:
        createUnion(i)

unionCnt = Counter(parent)
answer = unionCnt[parent[c]]

for i in sorted(unionCnt.keys(), key = lambda x: unionCnt[x], reverse= True):
    if k == 0: break
    if i not in set([parent[c], parent[h], 0]):
        answer += unionCnt[i]
        k -= 1

print(answer)

# bfs 정답 풀이

import sys
from collections import deque
from heapq import heappush, heappop
input = sys.stdin.readline

def bfs(i):
    queue = deque()
    queue.append(i)
    check[i] = i
    cnt = 1

    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if not check[nxt]:
                queue.append(nxt)
                check[nxt] = i
                cnt += 1
    return cnt

n, m = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

check = {i:0 for i in range(1, n+1)}
count_set = []
c, h, k = map(int, input().split())
for i in range(1, n+1):
    if not check[i]:
        cnt = bfs(i)
        heappush(count_set, (-cnt, i))
        if check[c] == i:
            answer = cnt

while count_set and k > 0:
    value, key = heappop(count_set)
    if check[key] != check[c] and check[key] != check[h]:
        answer -= value
        k -= 1

print(answer)