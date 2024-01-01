#2022.04.01
#수식 최대화

# 내 풀이
from itertools import permutations
import re

def solution(expression):
    max = 0
    tmp = 0
    ops = re.split('[0-9]+', expression)
    exp = re.split('([+*-])', expression)
    cases = permutations(set(ops[1:-1]))

    for case in cases:
        tmp1 = exp
        for op in case:
            while op in tmp1:
                idx = tmp1.index(op)
                if op == "*":
                    tmp = int(tmp1[idx-1]) * int(tmp1[idx+1])
                elif op == "+":
                    tmp = int(tmp1[idx-1]) + int(tmp1[idx+1])
                else:
                    tmp = int(tmp1[idx-1]) - int(tmp1[idx+1])
                tmp1 = tmp1[:idx-1] + tmp1[idx+2:]
                tmp1.insert(idx-1, str(tmp))
        if max < abs(int(''.join(tmp1))):
            max = abs(int(''.join(tmp1)))
    return max

# best 풀이 1 : 문자열 포매팅/eval 사용
def solution(expression):
    ops = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answers = []
    
    #튜플 앞에 있을수록 나중에 계산됨.
    for op in ops:
        op1 = op[0] # 세 번째(마지막)로 계산되는 연산자
        op2 = op[1] # 두 번째로 계산되는 연산자
        tmps = []
        # 문자열 포매팅으로 먼저 계산할 부분을 ()로 묶어준다.
        for exp in expression.split(op1):
            tmp = [f'({i})' for i in exp.split(op2)]
            tmps.append(f'({op2.join(tmp)})')
        # eval 함수를 통해서 문자열 식을 계산한다.
        answers.append(abs(eval(op1.join(tmps))))
    return max(answers)

# best 풀이 2 : eval/re.split() 사용
from itertools import permutations
import re

def solution(expression):
    answers = []
    ops = re.split('[0-9]+', expression)
    exp = re.split('([+*-])', expression)
    cases = permutations(set(ops[1:-1]))

    for case in cases:
        tmp1 = exp[:]
        for op in case:
            while op in tmp1:
                idx = tmp1.index(op)
                tmp1[idx-1] = str(eval(tmp1[idx-1] + op + tmp1[idx+1]))
                tmp1 = tmp1[:idx] + tmp1[idx+2:]
                
        answers.append(abs(int(tmp1[0])))
    return max(answers)