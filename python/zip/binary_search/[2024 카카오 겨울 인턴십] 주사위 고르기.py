# 1시간 30분

from itertools import combinations, product

result = 0
answer = []

def calResult(sum_a, sum_b):
    global result
    idxA = 0
    idxB = 0
    winCase = 0
    
    while len(sum_a) > idxA and len(sum_b) > idxB:
        if sum_a[idxA] > sum_b[idxB]:
            winCase += len(sum_a) - idxB
            idxA += 1
        else:
            idxB += 1
            
    if result < winCase:
        result = winCase
        return True
    else:
        return False
    
def diceSum(list):
    sums = []
    for case in product(*list):
        sums.append(sum(case))
    return sums

def play(dice, selected):
    global answer
    a = []
    b = []
    # a, b 배열로 분리
    for i in range(len(dice)):
        if i+1 in selected:
            a.append(dice[i])
        else:
            b.append(dice[i])
            
    # 합 모든 경우의 수 구하기
    sum_a = sorted(diceSum(a), reverse = True)
    sum_b = sorted(diceSum(b), reverse = True)
    if calResult(sum_a, sum_b):
        answer = selected

def solution(dice):
    idxs = range(1, len(dice)+1)
    # 주사위 절반을 뽑는 행위
    for case in combinations(idxs, len(dice)//2):
        play(dice, case)
        
    # 결과 반환
    return answer

# 이분 탐색 라이브러리 함수 활용

from itertools import combinations, product
from bisect import bisect_left

result = 0
answer = []

def calResult(sum_a, sum_b):
    global result
    winCase = sum(bisect_left(sum_b, num) for num in sum_a)
            
    if result < winCase:
        result = winCase
        return True
    else:
        return False
    
def diceSum(list):
    sums = []
    for case in product(*list):
        sums.append(sum(case))
    return sums

def play(dice, selected):
    global answer
    a = []
    b = []
    # a, b 배열로 분리
    for i in range(len(dice)):
        if i+1 in selected:
            a.append(dice[i])
        else:
            b.append(dice[i])
            
    # 합 모든 경우의 수 구하기
    sum_a = diceSum(a)
    sum_b = sorted(diceSum(b))
    if calResult(sum_a, sum_b):
        answer = selected

def solution(dice):
    idxs = range(1, len(dice)+1)
    # 주사위 절반을 뽑는 행위
    for case in combinations(idxs, len(dice)//2):
        play(dice, case)
        
    # 결과 반환
    return answer