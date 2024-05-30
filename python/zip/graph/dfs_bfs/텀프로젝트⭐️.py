import sys
input = sys.stdin.readline

# 팀이 되는 조건: 서클!
def checkCircle(n, preList, start):
    global candi
    candiList = []
    cur = start
    
    while 1:
        candiList.append(cur)
        visited[cur] = True
        cur = preList[cur - 1]
        
        # 서클이 생긴 경우
        if visited[cur]:
            if cur in candiList:
                candi |= set(candiList[candiList.index(cur):])
            return
            
t = int(input())
for _ in range(t):
    n = int(input())
    candi = set()
    preList = list(map(int, input().split()))
    
    visited = [False] * (n+1)
    for i in range(1, n+1):
        if not visited[i]:
            checkCircle(n, preList, i)
    print(n - len(candi))

# 재귀 dfs 풀이
import sys
sys.setrecursionlimit(10**6)

def dfs(x):
    global result
    visited[x] = True
    cycle.append(x)
    number = numbers[x]

    # 방문 가능한 곳인지 확인
    if visited[number]:
        # 사이클 가능한지 확인
        if number in cycle:
            result += cycle[cycle.index(number):]
        return
    else:
        dfs(number)

t = int(input())
for _ in range(t):
    n = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [True] + [False] * n
    result = []

    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n - len(result))