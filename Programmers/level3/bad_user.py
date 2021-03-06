#22.07.11
#불량 사용자

# 내 풀이
import re
answer = set()
dic = dict()

def makeStr(tmp):
    tmp1 = ['0' for _ in range(len(dic)+1)]
    for val in tmp:
        tmp1[dic[val]] = '1'
    return ''.join(tmp1)

def getAnswer(cases, idx, tmp):
    global answer
    if idx == len(cases):
        answer.add(makeStr(tmp))
        return
    for case in cases[idx]:
        if case not in tmp:
            getAnswer(cases, idx+1, tmp+[case])
        

def solution(user_id, banned_id):
    global answer, dic
    for i,val in enumerate(user_id):
        dic[val] = i
    cases = []
    for i in banned_id:
        case = []
        parts = i.split("*")
        regex = '[a-z0-9]'.join(parts)
        for j in user_id:
            if(re.match(regex, j) != None and len(i) == len(j)):
                case.append(j)
        cases.append(case)
    getAnswer(cases, 0, [])
    return len(answer)

# product 사용하기
# O(N^2)
import re
from itertools import product

def solution(user_id, banned_id):
    cases, answer = [], []
    for i  in banned_id:
        case = []
        parts = i.split("*")
        regex = '[a-z0-9]'.join(parts)
        for j in user_id:
            if re.match(regex, j) != None and len(i) == len(j):
                case.append(j)
        cases.append(case)
    results = list(product(*cases))
    for result in results:
        tmp = set(result)
        if len(tmp) == len(banned_id) and tmp not in answer:
            answer.append(tmp)
    return len(answer)