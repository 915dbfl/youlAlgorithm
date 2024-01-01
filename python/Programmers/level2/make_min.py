#22.05.11
#최솟값 만들기

# 내 풀이
def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse = True)
    for i in range(len(A)):
        answer += A[i] * B[i] 
    return answer

# 다른 풀이: zip 사용
def solution(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))