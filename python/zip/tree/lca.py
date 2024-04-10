import sys
input = sys.stdin.readline
from collections import defaultdict, deque

# O(nd) -> 100000
def bfs():
    que = deque()
    que.append(1)
    visited = [False] * (n+1)
    depth[1] = 1
    visited[1] = True

    while(que):
        cur = que.popleft()

        for nxt in dic[cur]:
            if (not visited[nxt]):
                parent[nxt] = cur
                depth[nxt] = depth[cur] + 1
                visited[nxt] = True
                que.append(nxt)
    
n = int(input())
edge = []
dic = defaultdict(list)

depth = [0] * (n+1)
parent = [0] * (n+1)
parent[1] = 1

for _ in range(n-1):
    n1, n2 = map(int, input().split(" "))
    dic[n1].append(n2)
    dic[n2].append(n1)

# 부모와 depth 구하기
bfs()

m = int(input())
# O(m * n)
# 운이 좋게 통과할 수 있었던 것 같다.
for _ in range(m):
    a, b = map(int, input().split(" "))

    # a에 항상 depth가 큰 값이 오게 수정
    if depth[a] < depth[b]:
        tmp = a
        a = b
        b = tmp

    # depth 맞추기
    depthA = depth[a]
    pA, pB = a, b
    while (depthA > depth[b]):
        pA = parent[pA]
        depthA -= 1

    for _ in range(depthA):
        if pA == pB:
            print(pA)
            break

        pA = parent[pA]
        pB = parent[pB]

# o(mlogn)의 시간복잡도를 가지도록 하자.
# 4/11
