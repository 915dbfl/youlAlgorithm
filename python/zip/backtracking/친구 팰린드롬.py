# 30분
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
prefer = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    prefer[a].append(b)
    prefer[b].append(a)

checked = [False] * (n+1)
answer = 1

# 시간복잡도: 2^n
def dfs(cur):
    global answer
    # 모든 학생을 다 확인했거나 / 이미 짝이 지어진 경우
    if cur > n or checked[cur]:
        tmpAns = sum(checked)
        tmpAns = tmpAns+1 if tmpAns+1 <= n else tmpAns
        if answer < tmpAns:
            answer = max(answer, tmpAns)
        return
    
    for f in prefer[cur]:
        # 이미 짝이 안지어진 경우
        if not checked[f]:
            checked[cur] = True
            checked[f] = True
            dfs(cur+1)
            checked[cur] = False
            checked[f] = False
    else:
        dfs(cur+1)

dfs(1)
print(answer)