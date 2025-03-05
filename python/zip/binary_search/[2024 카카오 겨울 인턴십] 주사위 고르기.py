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
    # 모든 주사위 play 조합 cnt 저장
    def play_case(lst):
        dices = []
        for num in lst:
            dices.append(dice[num-1])
        
        dict = defaultdict(int)
        for case in product(*dices):
            dict[sum(case)] += 1
    
        return dict
            
    # 해당 케이스 승률 구하기
    def cal_win(a, b):        
        a_dict = play_case(a)
        b_dict = play_case(b)
        
        winA = winB = 0
        for caseA, cntA in a_dict.items():
            for caseB, cntB in b_dict.items():
                if caseA > caseB:
                    winA += cntA * cntB
                elif caseB > caseA:
                    winB += cntA * cntB
        return winA, winB
    
    nums = range(1, len(dice)+1)
    best_case = []
    max_win = -1
    # 주사위 선택 조합 절반만 확인
    cases = list(combinations(nums, len(dice)//2))
    real_case = [[cases[i], cases[-1-i]] for i in range(len(cases)//2)]
    # a, b 승률 모두 구하기
    for a, b in real_case:
        winA, winB = cal_win(a, b)
        
        if max_win < winA:
            max_win = winA
            best_case = a
        if max_win < winB:
            max_win = winB
            best_case = b
    
    return sorted(best_case)