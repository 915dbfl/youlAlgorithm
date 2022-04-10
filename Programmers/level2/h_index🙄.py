#2022.04.10
#H-index
#테스트케이스 "질문하기" 참고해 추가 -> 해결!

#내 풀이
def solution(citations):
    citations.sort()
    h_index = 0
    for i in range(len(citations)):
        lef = len(citations[i:])
        if citations[i] == lef:
            return citations[i]
        elif citations[i] < lef:
            h_index = lef-1
        # 인용된 값들이 총 논문의 수보다 모두 클 경우 해당 코드 필요!
        else:
            h_index = max(h_index, lef)
    return h_index

#best 풀이1
def solution(citations):
    citations.sort(reverse = True)
    answer = max(map(min, enumerate(citations, start = 1)))
    return answer
#emerate에 start 값을 줌으로써 시작하는 숫자를 변경할 수 있다.

#best 풀이2
def solution(citations):
    citations.sort()
    l = len(citations)
    for i in range(l):
        if citations[i] >= (l-i):
            return l-i  
    return 0

