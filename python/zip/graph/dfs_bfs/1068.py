# brute force -> dfs, bfs
import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def removeChildOfTarget(target):
    dq = deque([target])

    while dq:
        cur = dq.popleft()
        child[parents[cur]] -= set([cur]) # 자식 제거
        parents[cur] = -2

        for c in child[cur]:
            dq.append(c)

def checkLeaf(start):
    dq = deque([start])
    cntLeaf = 0

    while dq:
        cur = dq.popleft()

        if parents[cur] != -2 and len(child[cur]) == 0:
            cntLeaf += 1
        else:
            for c in child[cur]:
                dq.append(c)

    print(cntLeaf)

n = int(input())
parents = list(map(int, input().split()))

root = -1
child = defaultdict(set)
for i in range(n):
    if parents[i] == -1:
        root = i
    else:
        child[parents[i]].add(i)

target = int(input())
removeChildOfTarget(target)
checkLeaf(root)