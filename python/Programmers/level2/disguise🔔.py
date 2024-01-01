#2022.04.08
#위장
#해시: key, value로 데이터가 저장되고, 검색과 저장이 O(1)로 무척 빠르다.

#내 풀이
def solution(clothes):
    dic = {}
    answer = 1
    for cloth in clothes:
        if cloth[1] not in dic.keys():
            dic[cloth[1]] = 1
        else: dic[cloth[1]] += 1
    for i in dic.values():
        answer *= i+1
    return answer -1

#best 풀이: Counter, reduce 사용!
from collections import Counter
from functools import reduce

def solution(clothes):
    cth = Counter(x[1] for x in clothes)
    return reduce(lambda x, y: x*(y+1), cth.values(), 1) -1
# reduce: 여러 개의 데이터를 대상으로 누적 집계를 낼 떼 사용!
# reduce(집계 함수, 순회 가능 데이터, 초기값)