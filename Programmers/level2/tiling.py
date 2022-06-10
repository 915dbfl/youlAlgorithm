#22.06.10
#타일링

#내 풀이
def solution(n):
    a, b = 1, 2
    
    for i in range(3, n+1):
        a, b = b, a+b
    return b % 1000000007