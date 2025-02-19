'''
주요 정보
- a, b: 도시를 짓기 위해 필요한 금 / 은의 양
- g: 각 도시의 금 양
- s: 각 도시의 은 양
- w: 각 도시의 트럭이 운반할 수 있는 최대 광물 양
- t: 각 도시의 트럭의 편도 걸리는 시간
=> 최소 시간 구하기

# 수식 도출 과정
- https://prgms.tistory.com/101
1. 결정 문제로 변환 -> T시간 안에 a, b를 운반할 수 있을까?
2. 두 가지 경우 고려
    - 금 최대, 은 최소
    - 금 최소, 은 최대
    -> 두 경우 모두 w[i]로 동일하다.
3. w[i]의 합이 a+b를 넘어야 한다.
    - 금을 최대, 은을 최대로 가져왔을 때
    - w[i]의 합이 a+b를 넘어야 한다.

# 시간 복잡도
1. log(Tmax): 이분 탐색으로 가능한 최소 시간을 찾음
2. n: 각 반복마다 전체 도시를 확인함
-> nlog(Tmax)
'''

def solution(a, b, g, s, w, t):
    start = 0
    end = 2 * 10**5 * 2 * 10**9
    
    while start <= end:
        mid = (start + end) // 2
        gold = 0
        silver = 0
        total = 0
        
        for i in range(len(g)):
            max_move = mid // (t[i] * 2)
            
            # 편도 이동할 수 있다면
            if (mid % (t[i] * 2)) >= t[i]:
                max_move += 1
                
            # 나른 광물 양 더해주기
            gold += g[i] if (g[i] <= (max_move * w[i])) else max_move * w[i]
            silver += s[i] if (s[i] <= (max_move * w[i])) else max_move * w[i]
            total += g[i] + s[i] if g[i] + s[i] < max_move * w[i] else max_move * w[i]
            
        if gold >= a and silver >= b and total >= a+b:
            end = mid - 1
        else:
            start = mid + 1
                
    return start