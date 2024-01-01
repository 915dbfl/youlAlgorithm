#2022.04.04
#예상 대진표

#내 풀이
def solution(n,a,b):
    while 1:
        n /= 2
        if a > n and b > n:
            a -= n
            b -= n
        elif not(a <= n and b <= n):
            return int(n*2-1).bit_length() #2의 몇 승인지 구함

#best 풀이 : 이진코드로 풀이
def solution(n, a, b):
    return ((a-1)^(b-1)).bit_length()

# best 풀이 : 배정받을 번호로 풀이
def solution(n,a,b):
    while a!=b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2
    return answer