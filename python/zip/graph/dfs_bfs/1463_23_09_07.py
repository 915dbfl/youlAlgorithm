# 1로 만들기
 
from collections import deque
n= int(input())

def bfs():
    dq = deque()
    dq.append((n, 0))
    visited = set([n])

    while dq:
        cur, cnt = dq.popleft()
        
        if cur == 1:
            print(cnt)
            return
        
        if cur % 3 == 0:
            dq.append((cur//3, cnt+1))
        if cur % 2 == 0:
            dq.append((cur//2, cnt+1))
        if cur > 1:
            dq.append((cur-1, cnt+1))

bfs()