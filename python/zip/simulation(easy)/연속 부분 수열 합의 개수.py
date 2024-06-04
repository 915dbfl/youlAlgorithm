# 프로그래머스
# 10분
def solution(elements):
    l = len(elements)
    # 원형 수열을 위해 배열 증가시키기
    elements = [0] + elements + elements
    # 누적합 구하기
    for i in range(1, len(elements)):
        elements[i] += elements[i-1]
    # 길이 1 - n까지 합 구하기
    answer = set()
    for i in range(1, l+1):
        p1, p2 = 0, i
        while p1 <= l:
            answer.add(elements[p2] - elements[p1])
            p1 += 1
            p2 += 1
            
    return len(answer)
        
# 다른 풀이
def solution(elements):
    l = len(elements)
    answer = set()
    
    # 기준점으로 부터 모든 길이를 구해 답에 추가
    for i in range(l):
        sum = elements[i]
        answer.add(sum)
        
        for j in range(i+1, i+l):
            sum += elements[j % l]
            answer.add(sum)
            
    return len(answer)