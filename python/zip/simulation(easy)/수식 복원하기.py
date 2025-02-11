"""
풀이과정 - 1시간 15분
1. 수식의 수들을 바탕으로 불가능한 진법 제외
2. 가능한 진법들로 수식 계산 -> 필터링
3. 진법 계산!
"""

def get_decimal(num, base):
    nums = list(map(int, list(num)))[::-1]
    pow = 0
    real_num = 0
    
    for n in nums:
        real_num += base**pow * n
        pow += 1
        
    return real_num

def get_base_num(real_num, base):
    nums = []
    
    while real_num >= base:
        nums.append(str(real_num % base))
        real_num //= base
    
    nums.append(str(real_num))
    return int("".join(nums[::-1]))
        
def get_base_nums(exps, max):
    possible = set()
    
    for i in range(max, 10):
        A = get_decimal(exps[0], i)
        B = get_decimal(exps[2], i)
        C = get_decimal(exps[4], i)
        
        expect = A + B if exps[1] == '+' else A - B
        if expect == C:
            possible.add(i)
                
    return possible       
    
def solution(expressions):
    unknowns = []
    unknowns = []
    Max = -1
    answer = []
    
    # 최소 진법 구하기
    for exp in expressions:
        exps = exp.split()
        for num in [exps[0], exps[2], exps[4]]:
            if num == 'X': 
                continue
            if len(num) == 1:
                Max = max(Max, int(num))
            else:
                Max = max(Max, int(num[0]))
                Max = max(Max, int(num[1]))

    # 가능한 진법 구하기
    candi = set(range(Max+1, 10))
    for exp in expressions:
        exps = exp.split()
        if exps[4] == 'X':
            unknowns.append(exps)
            continue
        else:
            candi &= get_base_nums(exps, Max+1)
               
    # 가려진 수식 결과 구하기
    for unks in unknowns:
        expect = -1
        for i in candi:
            A = get_decimal(unks[0], i)
            B = get_decimal(unks[2], i)
            
            result = get_base_num(A+B, i) if unks[1] == '+' else get_base_num(A-B, i)
            if expect == -1:
                expect = result
            if expect != result:
                answer.append(f'{unks[0]} {unks[1]} {unks[2]} = ?')
                break
        else:
            answer.append(f'{unks[0]} {unks[1]} {unks[2]} = {expect}')
        
    return answer