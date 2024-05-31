# 1번 헛간으로부터 거리가 가장 먼 헛간 찾기
# 14분

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, m = map(int, input().split())
dic = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

dq = deque()
dq.append((1, 0))
visited = [False] * (n+1)
visited[1] = True

answerL = []
dis = 0

while dq:
    cur, cnt = dq.popleft()

    if dis < cnt:
        answerL = [cur]
        dis = cnt
    elif dis == cnt:
        answerL.append(cur)
    
    for nxt in dic[cur]:
        if not visited[nxt]:
            dq.append((nxt, cnt+1))
            visited[nxt] = True

answerL.sort()
print(answerL[0], dis, len(answerL))