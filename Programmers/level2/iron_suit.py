#22.04.27
#점프와 순간 이동

#내 풀이
def solution(n):
    answer = 0
    while n != 0:
        if n % 2 == 0:
            n /= 2
        else:
            answer += 1
            n -= 1
    return answer

#비슷한 풀이
def solution(n):
    answer = 0
    while n > 0:
        answer += n%2
        n //= 2
    return answer

#best 풀이: 이진수 사용하기
def solution(n):
    return bin(n).count("1")