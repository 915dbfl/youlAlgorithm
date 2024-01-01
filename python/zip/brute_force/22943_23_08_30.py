# 수

# 풀이 - 시간초과
# k가지 수를 이용한 순열을 구한다.
# 순열 중 max까지의 소수들을 구하여 따로 배열에 저장한다.
# 소수들의 합으로 나타낼 수 있는 수를 구한다.
# 소수들의 곱으로 나타낼 수 있는 수를 구한다.
# 위 두 경우의 교집합을 구한다.

from itertools import permutations

k, m = map(int, input().split())
total = set()
Max = 0
for combi in permutations(list(map(str, range(10))), k):
    tmp = ("").join(combi)
    if tmp[0] != "0":
        Max = max(int(tmp), Max)
        total.add(int(tmp))

prime = [1] * (Max + 1)
prime[0] = prime[1] = 0
for i in range(2, Max+1):
    if prime[i] == 1:
        for j in range(i*2,  Max+1, i):
            prime[j] = 0

setPrimes = set()
for i in range(2, Max+1):
    if prime[i] == 1:
        setPrimes.add(i)

def isSumOfPrime(num):
    for i in setPrimes:
        if i != num-i:
            if num-i in setPrimes:
                return True
    else: return False

def isMulOfPrime(num):
    for i in setPrimes:
        if num % i == 0 and num//i in setPrimes:
                return True
    else: return False

cnt = 0
for case in total:
    if case >= m:
        while case % m == 0:
            case = case // m
    if isMulOfPrime:
        if isSumOfPrime:
            cnt += 1
print(cnt)

# 다른 풀이
# 짚고 넘어가야 할 것:
# 에라토스테네스의 체로 소수 구하기
# 소수들의 합으로 나타낼 수 있다면 같은 수로 나눈 값도 소수들의 합으로 나타낼 수 있음
# 소수들의 곱으로 나타내지지 않는다면 소수들의 합은 고려하지 않도록 함 
import sys
from itertools import permutations

k, m = map(int, input().split())
primes = [True] * 10**k

for i in range(2, int((10**k)**0.5)+1):
    if primes[i]:
        for j in range(i*i, 10**k, i):
            primes[j] = False

count = 0
for case in permutations(range(10), k):
    if case[0] == 0:
        continue
    num = int("".join(list(map(str, case))))
    temp = num
    while temp % m == 0:
        temp /= m
    for i in range(2, int(temp**0.5)+1):
        if temp%i == 0:
            if primes[i] and primes[temp//i]:
                for j in range(2, num//2):
                    if primes[j] and primes[num-j]:
                        count += 1
                        break
            break
        break

print(count)