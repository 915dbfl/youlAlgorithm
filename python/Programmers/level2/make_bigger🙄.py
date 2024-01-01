#22.04.14
#큰 수 만들기

#내 풀이(시간초과)
#파이썬 재귀 스택프레임이 갯수 제한 풀기!
import sys
sys.setrecursionlimit(10**6)

def getAnswer(number, k):
    m = max(number)
    idx = number.index(m)
    chk = len(number)-idx
    if k == 1:
        return m
    if k < chk:
        return m + getAnswer(number[idx+1:], k-1)
    elif k == chk:
        return number[idx:]
    else:
        return getAnswer(number[:idx],k-chk) + number[idx:]
    
def solution(number, k):
    return getAnswer(number, len(number) - k)