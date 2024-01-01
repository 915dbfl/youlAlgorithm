import sys
sys.setrecursionlimit(10**6)

def getResult(target):
    global answer
    if len(n) == 1:
        answer += 1
        return
    s = set(list(target))
    if len(s) == 1:
        answer += 1
        return
    else:
        getResult(target[1:])
        getResult(target[:-1])

answer = 0
n = input().rstrip()
getResult(n)
print(answer)

# =======================
# 완탐 리팩토링: 하나씩 쌓는 방법
import sys

# temp에 호출 숫자 순서대로 쌓이기 떄문에 중복 제외 가능
def dfs(left, right, cur, temp):
    if len(cur) == len_n:
        result.add(temp)
    if left > 0:
        dfs(left-1, right, n[left-1:right], temp + "".join(n[left-1:right]))
    if right < len_n:
        dfs(left, right+1, n[left:right+1], temp + "".join(n[left:right+1]))
    
n = input().rstrip()
result = set()
len_n = len(n)

for i in range(len_n):
    dfs(i, i, [], '')
print(len(result))