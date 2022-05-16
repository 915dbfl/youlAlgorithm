#22.05.16
#후보키

#내 풀이
from itertools import combinations

def solution(relation):
    answer = 0
    lstA = []
    lst = [[] for _ in range(len(relation[0]))]
    for case in relation:
        for i, val in enumerate(case):
            lst[i].append(val)
    nums = [str(i) for i in range(len(lst))]
    cnt = 1
    while cnt <= len(nums):
        for j in combinations(nums, cnt):
            for k in lstA:
                for c in k:
                    if c not in j:
                        break
                else:
                    break        
            else:
                tmp = [lst[int(case)] for case in j]
                chk = set(c for c in zip(*tmp))
                if len(chk) == len(relation):
                    answer += 1
                    lstA.append(''.join(j))
        cnt += 1
    return answer