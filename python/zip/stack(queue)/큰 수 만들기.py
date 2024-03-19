# 1. 최대값의 위치를 구한다.
# 2. 최대값의 위치까지 앞의 부분을 삭제할 수 있다면 삭제
    # 2-1. 최대값 고대로 출력!
    # 2-2. 최대값 이후의 위치에서 다시 과정을 반복한다.
# 3. 최대값의 위치까지 삭제할 수 없다면
    # 3-1. 최대값 이전의 위치에서 다시 과정을 반복한다.
    # 3-2. 최대값 이후의 값들은 고대로 출력!

# O(N**2)으로 시간 복잡도 초과

import sys
sys.setrecursionlimit(10**5)

def getAnswer(num, k):
    if k == 0 or len(num) == k:
        return ""
    elif sorted(num) == num:
        return num[k:]
    elif sorted(num, reverse = True) == num:
        return num[:-k]
    else:
        m = num.index(max(num))
        if m < k:
            k -= m
            return num[m] + getAnswer(num[m+1:], k)
        else:
            return getAnswer(num[:m], k) + num[m:]
            
def solution(number, k):
    return getAnswer(number, k)

# stack 활용하기

def solution(number, k):
    answer = []
    
    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
    return "".join(answer[:len(answer)-k])