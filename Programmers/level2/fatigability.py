#22.04.16
#피로도

#내 풀이
from itertools import permutations

def solution(k, dungeons):
    answer = set()
    for case in permutations(dungeons):
        tmp = k
        cnt = 0
        for i in case:
            if tmp >= i[0]:
                tmp -= i[1]
                cnt += 1
            else:
                answer.add(cnt)
                break
        else:
            answer.add(cnt)
    return max(answer)