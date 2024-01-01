#22.06.30
#줄 서는 방법

from math import factorial, ceil

def solution(n, k):
    lst = list(range(1, n+1))
    answer = []
    temp = factorial(n)
    
    while len(lst) > 0:
        temp //= n
        turn = ceil(k/temp)-1
        answer.append(lst.pop(turn))
        k -= temp*turn
        n -= 1
    return answer