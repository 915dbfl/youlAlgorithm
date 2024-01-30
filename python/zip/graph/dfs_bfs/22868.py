# dfs
import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def bfs(start, end):
    dq = deque([[start, set([start])]])
    visited = [0] * (n+1)
    visited[start] = 1

    while dq:
        cur, road = dq.popleft()

        if cur == end:
            return road

        for nxt in dic[cur]:
            if visited[nxt] != 1:
                visited[nxt] = 1
                dq.append([nxt, road | set([nxt])])

def bfs_with_rest(start, end, limit):
    dq = deque([[start, 0]])
    visited = [0] * (n+1)
    visited[start] = 1

    while dq:
        cur, dist = dq.popleft()

        if cur == end:
            return dist
    
        for nxt in dic[cur]:
            if (nxt in (start, end) or nxt not in limit) and visited[nxt] != 1:
                visited[nxt] = 1
                dq.append([nxt, dist+1])

dic = defaultdict(list)
n, m = map(int, input().split())
dist = []

# bfs 했을 때 가장 먼저 구해지는 경로가 사전 순에서 우선이도록 하기 위해 정렬
for _ in range(m):
    dist.append(list(map(int, input().split())))
dist.sort(key= lambda x: (x[0], x[1])) 

for a, b in dist:
    dic[a].append(b)
    dic[b].append(a)

s, e = map(int, input().split())

go_road = bfs(s, e)
cnt_back_raod = bfs_with_rest(e, s, go_road)

print(len(go_road) - 1 + cnt_back_raod)

# s->e path를 제외하기 위해
# visited에 1로 표시하는 방법 사용
import sys
from collections import defaultdict, deque
input = sys.stdin.readline
INF = sys.maxsize

def bfs(start, end):
    dq = deque([[start, set([start])]])

    while dq:
        cur, road = dq.popleft()

        if cur == end:
            return road

        for nxt in dic[cur]:
            if visited[nxt] != 1:
                visited[nxt] = 1
                dq.append([nxt, road | set([nxt])])

dic = defaultdict(list)
n, m = map(int, input().split())
dist = []

# bfs 했을 때 가장 먼저 구해지는 경로가 사전 순에서 우선이도록 하기 위해 정렬
for _ in range(m):
    dist.append(list(map(int, input().split())))
dist.sort(key= lambda x: (x[0], x[1])) 

for a, b in dist:
    dic[a].append(b)
    dic[b].append(a)

s, e = map(int, input().split())

result = 0
visited = [INF] * (n+1)
visited[s] = 1
go_road = bfs(s, e)

visited = [INF] * (n+1)
for i in go_road:
    visited[i] = 1
visited[s] = INF
back_road = bfs(e, s)

print(len(go_road)-1 + len(back_road)-1)