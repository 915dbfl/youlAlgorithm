# n을 만드는 방법의 수
# 처음 시작 수의 왼쪽 오른쪽에 수를 추가하는 방식
# 총 방법의 수는 몇 개일까?

# 백트래킹
from collections import defaultdict

n = input()
chars = defaultdict(int)
for i in list(n):
    chars[i] += 1

ans = 0
methods = []

def backTracking(x, path):
    global ans
    if len(x) == len(n):
        if x == n:
            ans += 1
        return
    for c, num in chars.items():
        if num == 0:
            continue
        # 양옆에 붙이기
        for nx in [c+x, x+c]:
            if n.find(nx) > -1 and path+[nx] not in methods:
                chars[c] -= 1
                methods.append(path+[nx])
                backTracking(nx, path+[nx])
                chars[c] += 1

backTracking('', [])
print(ans)

# 재귀함수
import sys
sys.setrecursionlimit(10**6)

def getResult(target):
    global answer
    s = set(list(target))
    if len(s) == 1:
        answer += 1
        return
    else:
        getResult(target[1:])
        getResult(target[:-1])

answer = 0
n = input().rstrip()
if len(n) == 1:
    print(1)
else:
    getResult(n)
    print(answer)

# dfs
import sys

n = input().rstrip()
result = set()
l = len(n)

def dfs(left, right, cur, temp):
    if len(cur) == l:
        result.add(temp)
    if left > 0:
        dfs(left - 1, right, n[left-1:right], temp + "".join(n[left-1:right]))
    if right < l:
        dfs(left, right+1, n[left:right+1], temp+ "".join(n[left:right+1]))

for i in range(l):
    dfs(i, i, [], '')
print(len(result))