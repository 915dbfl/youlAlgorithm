# 무조건 앞에 있는 parent와
# 무조건 뒤에 있는 child 구해
# 그 사이 등수 최대, 최소 출력

# 재귀
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def getChild(target):
    answer = set()
    visited[target] = True
    answer |= child[target]
    for ch in child[target]:
        # 방문하지 않은 곳만 방문
        if not visited[ch]:
            answer |= getChild(ch)

    return answer

def getParent(target):
    answer = set()
    visited[target] = True
    answer |= parent[target]
    for ch in parent[target]:
        # 방문하지 않은 곳만 방문
        if not visited[ch]:
            answer |= getParent(ch)

    return answer

n, m, x = map(int, input().split())

# parent, child 저장 딕셔러니
child = defaultdict(set)
parent = defaultdict(set)
# 한 번 방문한 곳 재방문할 필요 없음
visited = [False] * (n+1)

# 질문 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    child[a].add(b)
    parent[b].add(a)

parentCnt = len(getParent(x))
childCnt = len(getChild(x))

print(parentCnt + 1, n-childCnt)

# bfs 진행 -> 재귀보다 더 빠름
from collections import deque
import sys
input = sys.stdin.readline

n, m, x = map(int, input().split())
child = [[] for _ in range(n+1)]
parent = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    child[u].append(v)
    parent[v].append(u)

def bfs(graph):
    q = deque([x])
    visited = [False] * (n+1)

    while q:
        v = q.popleft()
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                q.append(u)
    return sum(visited)

print(bfs(parent)+1, n-bfs(child))