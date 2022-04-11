#2022.04.11
#카펫

#내 풀이

def solution(brown, yellow):
    plus = (brown + 4)//2
    for y in range(1, plus//2+1):
        if y * (plus - y) == brown + yellow:
            return [plus-y, y]