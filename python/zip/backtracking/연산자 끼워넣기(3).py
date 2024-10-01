import sys
from itertools import permutations
from collections import deque
input = sys.stdin.readline

n = int(input())
nums = list(input().split())
opNums = list(map(int, input().split()))
op = ["+", "-", "*", "//"]

ops = []
for i in range(4):
    for _ in range(opNums[i]):
        ops.append(op[i])

maxAns = -1000000000
minAns = 1000000000
calCase = set()

# O(10^7)
for case in permutations(ops):
    # 동일한 수식은 다시 계산하지 않음!⭐️
    if case in calCase: continue

    calCase.add(case)
    exp = deque([nums[0]])
    for i in range(len(case)):
        exp.append(case[i])
        exp.append(nums[i+1])
    
    result = int(eval("".join(exp)))
    maxAns = max(maxAns, result)
    minAns = min(minAns, result)

print(maxAns)
print(minAns)

# dfs 풀이

import sys
input = sys.stdin.readline

def dfs(expression, depth, use_cnt):
    global max_result, min_result
    if depth == N:
        tmp = eval(expression)
        max_result = max(max_result, tmp)
        min_result = min(min_result, tmp)
        return
    if use_cnt[0] < p_cnt:
        use_cnt[0] += 1
        dfs(expression + "+" + str(nums[depth]), depth + 1, use_cnt)
        use_cnt[0] -= 1
    if use_cnt[1] < mi_cnt:
        use_cnt[1] += 1
        dfs(expression + "-" + str(nums[depth]), depth + 1, use_cnt)
        use_cnt[1] -= 1
 
    if use_cnt[2] < mu_cnt:
        use_cnt[2] += 1
        dfs(expression + "*" + str(nums[depth]), depth + 1, use_cnt)
        use_cnt[2] -= 1
 
    if use_cnt[3] < d_cnt:
        use_cnt[3] += 1
        dfs(expression + "//" + str(nums[depth]), depth + 1, use_cnt)
        use_cnt[3] -= 1
 
 
N = int(input())
nums = list(map(int, input().split()))
p_cnt, mi_cnt, mu_cnt, d_cnt = map(int, input().split())
max_result, min_result = -float('inf'), float('inf')
dfs(str(nums[0]), 1, [0, 0, 0, 0])
print(max_result)
print(min_result)