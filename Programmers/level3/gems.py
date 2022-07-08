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