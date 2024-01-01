#22.05.02
#다음 큰 숫자

def solution(n):
    chk = bin(n).count("1")
    while 1:
        n += 1
        if bin(n).count("1") == chk:
            return n