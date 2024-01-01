#22.06.15
#보석 쇼핑

#내 풀이(시간초과)
def solution(gems):
    types = set(gems)
    dic = dict()
    for i, v in enumerate(gems):
        try:
            dic[v].append(i+1)
        except:
            dic[v] = [i+1]
    str = [x[0] for x in dic.values()]
    end = [x[-1] for x in dic.values()]
    answer = []
    for s in range(min(str), min(end)+1):
        for e in range(max(str), max(end)+1):
            if len(set(gems[s-1:e])) == len(types):
                answer.append([s,e])
    answer.sort(key = lambda x: (x[1]-x[0]+1, x[0]))
    return answer[0]