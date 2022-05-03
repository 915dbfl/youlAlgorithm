#22.05.03
#땅따먹기

#내 풀이
from copy import deepcopy

def solution(land):
    n = -1
    answer = 0
    for row in land:
        tmp = deepcopy(row)
        if n != -1:
            del(tmp[n])
        m = row.index(max(tmp))
        answer += row[m]
        n = m
    return answer
        