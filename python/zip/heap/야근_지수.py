from heapq import heappush, heappop

def solution(n, works):
    l = len(works)
    
    # 작업량 넣기
    hq = []
    for w in works:
        heappush(hq, [-w, w])
    
    # 작업량이 큰 값을 꺼내 -1 감소해주기
    while hq and n > 0:
        current = heappop(hq)
        newW = current[1] - 1
        if newW > 0:
            heappush(hq, [-newW, newW])
        n -= 1
        
    answer = 0
    while hq:
        current = heappop(hq)
        answer += current[1]**2
        
    return answer