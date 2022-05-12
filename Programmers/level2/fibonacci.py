#22.05.12
#피보나치 수

#내 풀이
def solution(n):
    answer = [0, 1]
    for _ in range(2, n+1):
        answer.append(answer[-1]+answer[-2])
    return answer[-1] % 1234567

#다른 풀이
def solution(n):
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a+b
    return b % 1234567