# 30분
from collections import defaultdict

def solution(want, number, discount):
    dcDict = defaultdict(int)
    dl = len(discount)
    wl = len(want)
    
    p1, p2 = 0, 0
    # dict 초기화
    for i in range(10):
        p2 = i
        dcDict[discount[p2]] += 1
    
    answer = 0
    while p2 < dl:
        # 원하는 제품을 모두 할인 받을 수 있는 날짜인지 확인
        for i in range(wl):
            if dcDict[want[i]] != number[i]:
                break
        # 모든 경우를 만족했을 때만
        else:
            answer += 1
        
        if p2 + 1 < dl:
            dcDict[discount[p1]] -= 1; p1 += 1
            p2 += 1; dcDict[discount[p2]] += 1
        else:
            break
        
    return answer

# Counter 활용 풀이
from collections import Counter

def solution(want, number, discount):
    answer = 0
    dic = {}
    
    # want 값들 dict으로 만들기
    for i in range(len(want)):
        dic[want[i]] = number[i]
        
    for i in range(len(discount) - 9):
        if dic == Counter(discount[i:i+10]):
            answer += 1
            
    return answer