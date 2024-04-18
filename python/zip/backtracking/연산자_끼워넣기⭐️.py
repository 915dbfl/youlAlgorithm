# 순열 활용
import sys
from itertools import permutations
input = sys.stdin.readline

def calculate(ops, n):
    global Max, Min
    result = nums[0]

    for i in range(n-1):
        if ops[i] == "+":
            result += nums[i+1]
        elif ops[i] == "-":
            result -= nums[i+1]
        elif ops[i] == "*":
            result *= nums[i+1]
        else:
            if result < 0:
                result =  -(abs(result)//nums[i+1])
            else:
                result //= nums[i+1]
    
    if Max < result:
        Max = result
    if Min > result:
        Min = result

n = int(input())
nums = list(map(int, input().split()))
Max = -sys.maxsize
Min = sys.maxsize

# ops 개수만큼 배열에 넣기
ops = []
count = list(map(int, input().split()))
for i in range(4):
    if i == 0: # 덧셈
        for i in range(count[i]):
            ops.append("+")
    elif i == 1: # 뺄셈
        for i in range(count[i]):
            ops.append("-")
    elif i == 2: # 곱셈
        for i in range(count[i]):
            ops.append("*")
    else:
        for i in range(count[i]):
            ops.append("/")

for case in permutations(ops):
    calculate(case, n)

print(Max)
print(Min)

# 백트레킹 활용⭐️
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))

Max = -sys.maxsize
Min = sys.maxsize

def dfs(depth, total, plus, minus, multiply, divide):
    global Max, Min
    if depth == n:
        Max = max(total, Max)
        Min = min(total, Min)
        return
    
    if plus: dfs(depth + 1, total + num[depth], plus -1 , minus, multiply, divide)
    if minus: dfs(depth + 1, total - num[depth], plus, minus-1, multiply, divide)
    if multiply: dfs(depth + 1, total * num[depth], plus, minus, multiply-1, divide)
    if divide: dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide-1)

dfs(1, num[0], op[0], op[1], op[2], op[3])
print(Max)
print(Min)