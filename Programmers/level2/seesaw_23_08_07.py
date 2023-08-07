# 시소 짝꿍

#시간 초과
from collections import defaultdict
from itertools import combinations

def solution(weights):
    dic = defaultdict(list)
    result = set()
    
    # 사람 무게 * 좌석 간의 거리 곱이 w*i인 모든 경우
    for i in range(len(weights)):
        for j in range(2, 5):
            dic[weights[i]*j].append(i)
            
    # 사람 무게 * 좌석 간의 거리 곱이 w*i인 경우 모든 시소짝꿍 구하기
    for k in dic.keys():
        for a, b in combinations(dic[k], 2):
            tmp = (a, b) if a < b else (b, a)
            result.add(tmp)
             
    return len(result)

# 다른 풀이
from collections import defaultdict
from itertools import combinations

def solution(weights):
    dic = defaultdict(int)
    answer = 0
    
    for w in weights:
        dic[w] += 1
        
    for k in dic.keys():
        s = dic[k]
        if s >= 2:
            answer += s * (s-1) // 2
            
    weights = set(weights)
    for w in weights:
        answer += dic[w] * dic[w*3/2]
        answer += dic[w] * dic[w*2]
        answer += dic[w] * dic[w*4/3]
                
    return answer
        