#23.02.18
#프린터 큐
#알고리즘 스터디: 시뮬레이션

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, t = map(int, input().split())
    lst = list(input().split())
    q = deque()
    order = 1

    for i, n in enumerate(lst):
        q.append((i, n))


    while q:
        i, n = q.popleft()

        if max(lst) == n:
            if i == t:
                print(order)
                break
            lst.remove(n)
            order += 1

        else:
            q.append((i, n))

# 다른 풀이
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, t = map(int, input().split())
    index = deque(list(range(n)))
    priority = deque(list(map(int, input().split())))
    cnt = 0

    while 1:

        if priority[0] == max(priority):
            cnt += 1

            priority.popleft()

            if index.popleft() == t:
                print(cnt)
                break
        else:
            priority.append(priority.popleft())
            index.append(index.popleft())