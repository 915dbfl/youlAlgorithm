#23년 8월 16일
#n과 m(10)

from itertools import combinations

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
stack = []
check = set()
answer = ""

def dfs(cur):
    global answer
    if len(stack) == m:
        tmp1 = tuple(stack)
        if tmp1 not in check:
            tmp2 = list(map(str, stack))
            check.add(tmp1)
            answer += " ".join(tmp2) + "\n"
            return
        else:
            return
    
    if cur == n:
        return
    
    stack.append(lst[cur])
    dfs(cur+1)
    stack.pop()
    dfs(cur+1)

dfs(0)
print(answer)
