#22.05.14
#큰 수 만들기

# 내 풀이(시간 초과)
import sys
sys.setrecursionlimit(10**6)

def getAnswer(num, k):
    if k == 0 or len(num) == k:
        return ""
    elif sorted(num) == num:
        return num[k:]
    elif sorted(num, reverse = True) == num:
        return num[:-k]
    else:
        m = num.index(max(num))
        if m <= k:
            k -= m
            return num[m] + getAnswer(num[m+1:], k)
        else:
            return getAnswer(num[:m], k) + num[m:]
            
def solution(number, k):
    return getAnswer(number, k)