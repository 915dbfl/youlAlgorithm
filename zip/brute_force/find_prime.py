#22.09.19(brute force/완전 탐색)
#level 2

#내 풀이 : 모든 조합을 찾은 후 각각 소수인지를 판단한다.
from itertools import permutations

def checkPrime(num):
    if num == 1 or num == 0:
        return False
    if num == 2:
        return True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    else:
        return True   

def solution(numbers):
    lst = list(map(str, numbers))
    zip = []
    for i in range(1, len(numbers)+1):
        zip += permutations(lst, i)
        
    zip = set(map(lambda x: int(''.join(x)), zip))
    count = 0
    for i in zip:
        if checkPrime(i):
            count += 1
    return count
 
        
# best 풀이: set의 차/합집합을 사용한 풀이
from itertools import permutations

def solution(numbers):
    group = set()
    for i in range(1, len(numbers)+1):
        group |= set(map(int, map("".join, permutations(list(numbers), i))))
        
    group -= set(range(2))
    for i in range(2, int(max(group)**0.5)+1):
        group -= set(range(i*2, max(group)+1, i))
        
    return len(group)