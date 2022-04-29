#22.04.28
#n^2 배열 자르기

#내 풀이
def solution(n, left, right):
    answer = []
    num = (left+1)%n if (left+1)%n != 0 else n
    round = left//n+1
    for _ in range(right-left+1):
        if round > num:
            answer.append(round)
        else:
            answer.append(num)
        if num == n:
            round+=1
        num = num+1 if num != n else 1

    return answer