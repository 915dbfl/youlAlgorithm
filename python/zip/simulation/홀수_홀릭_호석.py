# 브루트 포스
# 입력되는 n <= 100000000
# n의 최대 길이 10 -> 브루트 포스 가능

import sys
from itertools import combinations
input = sys.stdin.readline

n = input().rstrip()
# 홀수의 개수를 저장하는 변수
result = []

def calculate(base, oddCnt):
    # 현재 str에서 홀수의 개수 구하기
    curOdd = 0
    for s in base:
        if int(s) % 2 == 1:
            curOdd += 1

    if len(base) == 1:
        result.append(oddCnt+curOdd)
        
    elif len(base) == 2:
        f = base[0]
        s = base[1]
        n = str(int(f) + int(s))
        calculate(n, oddCnt + curOdd)

    elif len(base) > 2:
        nums = [i for i in range(1, len(base))]

        for p1, p2 in combinations(nums, 2):
            f = base[:p1]
            s = base[p1:p2]
            t = base[p2:]
            n = str(int(f) + int(s) + int(t))
            calculate(n, oddCnt + curOdd)

calculate(n, 0)
result.sort()
print(result[0], result[-1])