#2022.03.30
#가장 큰 수

#내 풀이
def solution(numbers):
    answer = ""
    lst = [[i, str(v)] for i, v in enumerate(numbers)]
    for i in range(len(lst)):
        l = len(lst[i][1])
        if l == 1:
            lst[i][1] += lst[i][1][0]*3
        elif l == 2:
            lst[i][1] += lst[i][1]
        elif l == 3:
            lst[i][1] += lst[i][1][0]
    lst.sort(key = lambda x: x[1], reverse = True)
    for i in lst:
        answer += str(numbers[i[0]])        
    return str(int(answer))

#best 풀이1🔔🔔🔔🔔🔔
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse = True)
    # 숫자 반복? 같은 숫자 패턴의 숫자들을 비교하기 위함.
    # 같은 숫자 패턴의 경우: 숫자를 반복해 해당 숫자가 앞에 왔을 경우, 만들 수 있는 최대를 만들기 위해서이다.
    return str(int(''.join(numbers)))

#best 풀이2 : cmp_to_key사용🔔🔔🔔
from functools import cmp_to_key

def compares(x, y):
    tmp1 = int(x+y)
    tmp2 = int(y+x)
    return (tmp1 > tmp2) - (tmp1 < tmp2)

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = cmp_to_key(compares), reverse = True)
    return str(int(''.join(numbers)))