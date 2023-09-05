# 두 큐 합 같게 만들기: 틀림

# 합의 크기가 더 큰 큐에서 다른 큐로 이동
# 하나의 큐가 empty가 될 때까지 반복
from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    t1 = sum(queue1)
    t2 = sum(queue2)
    
    cnt = 0
    for i in range(300000):
        if t1 > t2:
            tmp = queue1.popleft()
            queue2.append(tmp)
            t1 -= tmp
            t2 += tmp
        elif t1 < t2:
            tmp = queue2.popleft()
            queue1.append(tmp)
            t2 -= tmp
            t1 += tmp
        else:
            return i
    else:
        return -1
            
