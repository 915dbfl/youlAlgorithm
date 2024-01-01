# gcd 합

import sys
from itertools import combinations
from math import gcd

t = int(input())
for _ in range(t):
    lst = list(map(int, sys.stdin.readline().split()))
    answer = 0

    for case in combinations(lst[1:], 2):
        tmp = case[0]
        for j in range(1, len(case)):
            tmp = gcd(tmp, case[j])
        answer += tmp

    print(answer)

# 다른 풀이
for _ in range(t):
    lst = list(map(int, sys.stdin.readline().split()))
    answer = 0

    for i in range(1, len(lst)):
        for j in range(i+1, len(lst)):
            answer += gcd(lst[i], lst[j])

    print(answer)

# 유클리드 호제법
def get_gcd(a, b):
    if b == 0:
        return a
    else:
        get_gcd(b, a%b)