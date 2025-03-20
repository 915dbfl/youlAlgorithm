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

# 30분
"""
# 풀이 과정
- 특정 주사위를 선택해야 하는 명확한 이유가 없음
- 그리고 승률을 구해야 하기 때문에 모든 경우를 확인해야 함
- 시간 복잡도 줄이기
    - 전체 조합을 확인하지 않아도 된다.
    - 결국 a를 제외하면 b가 선택하게 되니, a / b의 승률을 모두 구해서 활용
"""

from itertools import combinations, product
from collections import defaultdict

def solution(dice):
    dice_num = set(range(1, len(dice) + 1))
    max_win = -1
    combi = []
    
    def play(me, other):
        me_dict = defaultdict(int)
        other_dict = defaultdict(int)
        
        for case in product(*list(dice[i-1] for i in me)):
            me_dict[sum(case)] += 1
        
        for case in product(*list(dice[i-1] for i in other)):
            other_dict[sum(case)] += 1
            
        me_win = other_win = 0
        for (mk, mv) in me_dict.items():
            for (ok, ov) in other_dict.items():
                if mk > ok:
                    me_win += mv * ov
                elif mk < ok:
                    other_win += mv * ov
                    
        is_win = me_win > other_win
        total_win = me_win if is_win else other_win
        
        return [is_win, total_win]
    
    for case in combinations(dice_num, len(dice) // 2):
        me = case
        other = dice_num - set(case)
        
        result, case_win = play(me, other)
        if case_win > max_win:
            max_win = case_win
            combi = me if result else other
            
    return sorted(combi)