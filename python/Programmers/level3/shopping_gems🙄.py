#22.07.08
#보석 쇼핑

#효율성 통과 못함
def solution(gems):
    type = len(set(gems))
    l = len(gems)
    if type == 1:
        return [1, 1]
    elif type == l:
        return [1, type]
    else:
        answer = [1, l]
        s, e = 0, 0
        tmp = set()
        while s <= e and e < l and answer[1] - answer[0] + 1 != type:
            if len(tmp) == type:
                if answer[1]-answer[0] > e-s:
                    answer = [s+1, e+1]
                s += 1
            else:
                e += 1
            tmp = set(gems[s:e+1])
        return answer

# 베스트 풀이
from collections import defaultdict

def solution(gems):
    num = len(set(gems))
    result = []
    dic = defaultdict(int)

    left = 0
    best = 0
    for right in range(len(gems)):
        dic[gems[right]] += 1
        right += 1
        while len(dic) == num:
            dic[gems[left]] -= 1
            if dic[gems[left]] == 0:
                del dic[gems[left]]
            left += 1
            best = 1
        if best: 
            result.append([left, right])
            best = 0

    return sorted(result, key = lambda x: (x[1]-x[0], x[0]))[0]