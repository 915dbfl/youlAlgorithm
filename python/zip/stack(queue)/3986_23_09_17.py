# 좋은 단어

# stack, deque
import sys
from collections import deque

n = int(sys.stdin.readline())
result = 0
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    dq = deque(word[0])

    for i in range(1, len(word)):
        if len(dq) == 0:
            dq.append(word[i])
        else:
            if word[i] == dq[-1]:
                dq.pop()
            else:
                dq.append(word[i])
        

    if len(dq) == 0:
        result += 1

print(result)