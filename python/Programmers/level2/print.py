#2022.03.28
#프린터

#내 풀이
def solution(priorities, location):
    answer = 0
    
    while 1:
        if max(priorities) <= priorities[0]:
            answer += 1
            priorities.pop(0)
            if location == 0:
                return answer
        else:
            priorities.append(priorities.pop(0))
        location = location -1 if location != 0 else len(priorities)-1

#best 풀이
def solution(priorities, location):
    answer = 0
    q = [(i, p) for i, p in enumerate(priorities)]
    
    while 1:
        cur = q.pop(0)
        if any(cur[1] < i[1] for i in q):
            q.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

# any(반복 가능한 자료형): 반복 가능한 자료형 중 하나라도 True가 있을 경우 True, 아니면 False
# all(반복 가능한 자료형): 반복 가능한 자료형 중 전체가 True면 True, 아니면 False