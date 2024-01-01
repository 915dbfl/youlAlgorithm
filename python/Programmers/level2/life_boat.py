#22.04.22
#구명보트

#내 풀이(시간초과)
def solution(people, limit):
    answer = 0
    chk = [0 for i in range(len(people))]
    people.sort()
    for i in range(len(people)):
        if chk[i] == 0:
            for j in range(len(people)-1, i, -1):
                if chk[j] == 0 and people[i] + people[j] <= limit:
                    chk[j] = 1
                    break
            answer += 1
            chk[i] = 1
    return answer

# 질문 참고해 다시 작성한 풀이
from collections import deque
from math import ceil

def solution(people, limit):
    answer = 0
    people.sort(reverse = True) # 역순으로 정렬
    p = deque(people)
    while len(p) >= 2 and p[0] >= limit//2: # 가장 큰 무게가 제한무게의 절반보다 클 경우
        if p[0] + p[-1] <=limit: # 무게가 가장 적게 나가는 사람과 같이 태울 수 있을 경우
            p.pop()
        p.popleft() # 그렇지 못할 경우
        answer += 1
    answer += ceil(len(p)/2) # 모든 사람 무게가 제한무게의 절반보다 적으므로 2명씩 함께 태울 수 있다.
    return answer

# best 풀이1 : 전체 수에서 같이 타는 사람수 제외시키기
def solution(people, limit):
    answer = 0
    people.sort()
    
    min = 0
    max = len(people)-1
    
    while min < max:
        if people[min] + people[max] <= limit:
            min += 1
            answer += 1
        max -= 1
    return len(people) - answer
        

# best 풀이2: deque를 사용한 풀이
from collections import deque

def solution(people, limit):
    answer = 0
    dq = deque(sorted(people))
    
    while dq:
        min = dq.popleft() # 가장 적은 무게
        if not dq:
            return answer + 1
        max = dq.pop() # 가장 큰 무게
        if min + max > limit: # 두 사람을 같이 못 태울 경우
            dq.appendleft(min) # 큰 무게의 사람만 보트에 태운다.
        answer += 1
    return answer