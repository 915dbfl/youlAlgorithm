#23.07.17
#숫자야구

import sys
from itertools import permutations

n = int(input())
data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
num = list(permutations(data, 3))

for _ in range(n):
    n, s, b = map(int, sys.stdin.readline().split())
    n = str(n)
    rm_cnt = 0 # 

    for i in range(len(num)):
        strike = ball = 0
        i -= rm_cnt # remove로 삭제된 값이 있더라도 num[0]로 시작하기 위해

        for j in range(3):
            if num[i][j] == n[j]:
                strike += 1
            elif n[j] in num[i]:
                ball += 1

        if (strike != s) or (ball != b):
            num.remove(num[i])
            rm_cnt += 1
print(len(num))