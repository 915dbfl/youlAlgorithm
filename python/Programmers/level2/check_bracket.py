#22.05.02
#올바른 괄호

def solution(s):
    answer = 0
    for i in s:
        if i == ")":
            answer -= 1
        else:
            answer += 1
        if answer < 0:
            return False
    return answer == 0