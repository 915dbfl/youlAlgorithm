#22.07.02
#행렬의 곱셈

def solution(a, b):
    answer = []
    for i in a:
        temp = []
        for j in range(len(b[0])):
            result = 0
            for index, value in enumerate(i):
                result += value*b[index][j]
            temp.append(result)
        answer.append(temp)
    return answer

# best 풀이: zip사용
def solution(arr1, arr2):
    answer = []
    for i in arr1:
        temp = []
        for j in zip(*arr2):
            temp.append(sum(a*b for a,b in zip(i, j)))
        answer.append(temp)
    return answer

# numpy 모듈 사용
from numpy import matrix
def solution(arr1, arr2):
    return (matrix(arr1)*matrix(arr2)).tolist()