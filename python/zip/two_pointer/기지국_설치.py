# 5g 기지국을 최소로 설치

# n <= 200,000,000이므로 O(n)보다 적어야 함
# stations의 크기를 활용하자

# 문제 풀이
    # 1. 현재 도달하는 아파트 표시
    # 2. 도달되지 않는 범위 구하기 -> 최소 증설 개수 구하기
from math import ceil
    
def solution(n, stations, w):
    # 전파 도달 idx
    start = 1
    end = 1
    cnt = 0
    
    for s in stations:
        if start > n:
            break
        
        # stations의 전파가 도달하는 위치 왼쪽 범위
        end = s - w
        # 새로운 도달 범위가 전파 도달 완료된 위치보다 왼쪽이라면
        if end <= start:
            start = s + w + 1
        # 전파 도달하지 않는 범위가 존재할 떄
        else:
            # 전파 증설
            diff = end - start
            cnt += ceil(diff / (w*2+1))
            start = s + w + 1
            
    # 끝에서 채워지지 않은 부분 채우기
    if start <= n:
        diff = n - start + 1
        cnt += ceil(diff / (w*2+1))
    
    return cnt