#22.09.19
#모음 사전

# 내 풀이: 모든 경우의 수를 구해 해당 값의 위치를 파악하자
# 최대 길이가 5로 크지 않으므로 완전탐색을 사용할 수 있다.
# big time_complexity
from itertools import product

def solution(word):
    dic = []
    
    for i in range(1, 6):
        dic += list(map("".join, product('AEIOU', repeat = i)))
            
    dic.sort()
    return dic.index(word) + 1
    
# 다른 풀이: 해당 자리에서 다음 문자 간의 거리를 이용한 풀이
def solution(word):
    max = 0
    for i in range(1, 6):
        max += 5**i
        
    result = 0
    for i in range(len(word)):
        if word[i] == "A":
            result += 1
        elif word[i] == "E":
            result += max//(5**(i+1))*1+1
        elif word[i] == "I":
            result += max//(5**(i+1))*2+1
        elif word[i] == "O":
            result += max//(5**(i+1))*3+1
        else:
            result += max//(5**(i+1))*4+1
    
    return result
    
# 다른 풀이: 등비수열의 식 이용
def solution(word):
    answer = 0
    
    for i, a in enumerate(word):
        answer += (5**(5-i)-1)/4 * "AEIOU".index(a) + 1

    return answer