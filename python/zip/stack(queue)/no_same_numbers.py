#22.09.21
#level1
#같은 숫자는 싫어

# 내 풀이
def solution(arr):
    b = -1
    result = []

    for i in arr:
        if b != i:
            result.append(i)
            b = i

    return result

# 슬라이싱 적용
def solution(arr):
    result = []
    
    for i in arr:
        if result[-1:] != [i]:
            result.append(i)

    return result