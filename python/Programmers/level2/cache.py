#22.04.25
#[1차]캐시
#LRU : 가장 오랫동안 사용되지 않은 것을 교체
#LFU : 가장 적게 참조된 것을 교체

#내 풀이
from collections import deque

def solution(cacheSize, cities):
    cities = [s.upper() for s in cities]
    answer = 0
    cache = deque()
    if cacheSize == 0:
        return 5 * len(cities)
    for city in cities:
        if city in cache:
            #🌟내가 헷갈렸던 부분
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            if len(cache) >= cacheSize:
                cache.popleft()
            cache.append(city)
            answer += 5
    return answer

# BEST 풀이: deque의 maxlen 설정!
# 제한된 길이에 따라서 왼쪽으로 값을 추가할 경우, 가장 오른쪽 값이 삭제되고
# 오른쪽으로 값을 추가할 경우, 가장 왼쪽 값이 삭제된다.
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen = cacheSize)
    for i in cities:
        s = i.lower()
        if s in cache:
            answer += 1
            cache.remove(s)
            cache.append(s)
        else:
            answer += 5
            cache.append(s)
    return answer
