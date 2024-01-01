#n과 m(2)
#23.06.27

#combination
import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
arrays = [i for i in range(1, n+1)]

for case in combinations(arrays, m):
    # *를 통한 unpakcing
    print(*list(case))

#backtracking
import sys

def dfs(v):
    global visited, answer, m
    if len(answer) == m:
        print(*answer)
        return
    elif v < n:
        answer.append(arrays[v])
        dfs(v+1)
        answer.pop()
        dfs(v+1)

n, m = map(int, sys.stdin.readline().split())
arrays = [i for i in range(1, n+1)]
answer = []

dfs(0)

# backtracking 다른 풀이
n, m = map(int, sys.stdin.readline().split())
answer = []

def dfs(cur):
    if len(answer) == m:
        print(*answer)
        return
    
    for i in range(cur, n+1):
        if i not in answer:
            answer.append(i)
            dfs(i+1)
            answer.pop()

dfs(1)