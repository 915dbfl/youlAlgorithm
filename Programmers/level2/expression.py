#22.05.13
#숫자의 표현

#내 풀이
def solution(n): 
    answer = 1
    for i in range(1, n//2+1):
        lst = [i]
        while sum(lst) <= n:
            if sum(lst) == n:
                answer += 1
                break
            else:
                lst.append(lst[-1]+1)
    return answer