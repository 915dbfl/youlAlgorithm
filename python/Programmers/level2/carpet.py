#2022.04.11
#카펫

#내 풀이
def solution(brown, yellow):
    plus = (brown + 4)//2
    for y in range(1, plus//2+1):
        if y * (plus - y) == brown + yellow:
            return [plus-y, y]

#근의 공식 사용하기
# xy = brown + yellow
# (x-2)(y-2) = yellow
def solution(brown, yellow):
    a = (brown + 4 + ((brown + 4) ** 2 - 16 * (brown + yellow)) ** 0.5) / 4
    b = (brown + yellow) / a
    return [max(a,b), min(a,b)]