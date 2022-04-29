#22.04.29
#스킬 트리

#내 풀이: 시간이 많이 소요되는 방식
def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        lst = []
        for i in skill:
            if i in tree:
                lst.append(tree.index(i))
            else:
                lst.append(27)
        if lst == sorted(lst):
            answer += 1
    return answer


#다른 풀이 : popleft()를 통해서 순서 확인하기
from collections import deque

def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        tmp = deque(skill)
        for i in tree:
            if i in tmp:
                if i != tmp.popleft():
                    break
        else:
            answer += 1
    return answer

#다른 풀이: 트리 내 요소일 경우 차례대로 추가해 트리와 일치하는지 확인
def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        tmp = ""
        for i in tree:
            if i in skill:
                tmp += i
        if tmp == skill[:len(tmp)]:
            answer += 1
    return answer