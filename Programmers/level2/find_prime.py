#2022.04.02
#소수 찾기

#내 풀이
from itertools import permutations

#에라토스테네스 체 생성!
def getPrime():
    lst = [1 for i in range(10000000)]
    lst[1] = 0; lst[0] = 0
    for i in range(2, int(9999999**0.5) + 1):
        if lst[i] == 1:
            for j in range(i*2, 10000000, i):
                lst[j] = 0
    return lst      

def solution(numbers):
    answer = 0
    a = set()
    lst = getPrime()
    for i in range(len(numbers)):
        a |= set(map(int, map(''.join, permutations(list(numbers), i+1))))
    a -= set(range(2))
    for i in a:
        if lst[i] == 1:
            lst[i] = 3
            answer += 1
    return answer


#best 풀이 : 에라토스테네스 체에 set 적용하기
from itertools import permutations

def solution(numbers):
    a = set()
    for i in range(1, len(numbers)+1):
        a |= set(map(int, map(''.join, permutations(list(numbers), i))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a)**0.5)+1):
        a -= set(range(i*2, max(a)+1, i))
    return len(a)

#다른 풀이 : 재귀 사용
primeSet = set()

def isPrime(num):
    if num in (0, 1):
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def makeCombi(str1, str2):
    if str1 != "":
        if isPrime(int(str1)):
            primeSet.add(int(str1))
          
    # 경우의 수를 만드는 방식이 새로움!
    for i in range(len(str2)):
        makeCombi(str1 + str2[i], str2[:i] + str2[i+1:])

def solution(numbers):
    makeCombi("", numbers)
    return len(primeSet)

# 튜플도 join함수의 인자로 가능하다.
# permutations에 요소의 길이를 설정할 수 있다.
# |나 |=를 통해서 set, dictionary, counter를 합칠 수 있다.
# set(range(?))처럼 for문을 돌리지 않고 값을 생성할 수 있다.
  # list(range(?))도 마찬가지이다.