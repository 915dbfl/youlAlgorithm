# 30분
from itertools import product

tc = int(input())
op = [' ', '+', '-']
for i in range(tc):
    n = int(input())
    if i > 0:
        print()
    for case in product(op, repeat=n-1):
        exp = []
        for i in range(1, n):
            exp.append(str(i))
            exp.append(case[i-1])
        exp.append(str(n))
        
        ans = ''.join(exp)
        expStr = ans.replace(" ", "")
        if eval(expStr) == 0:
            print(ans)

# 재귀 호출
import sys
input = sys.stdin.readline

def cal(ops):
    result_str = ""
    for i in range(len(ops)):
        result_str += str(i+1)
        result_str += ops[i]
    result_str += str(len(ops) + 1)

    real_result = result_str.replace(" ", "")
    return [eval(real_result), result_str]

def dfs(n, ops, index):
    if index == n - 1:
        result = cal(ops)
        if result[0] == 0:
            print(result[1])
        return

    dfs(n, ops, index + 1)
    ops[index] = '+'
    dfs(n, ops, index + 1)
    ops[index] = '-'
    dfs(n, ops, index + 1)
    ops[index] = ' '

tc = int(input())
for _ in range(tc):
    n = int(input())
    ops = [' '] * (n-1)
    dfs(n, ops, 0)
    print()