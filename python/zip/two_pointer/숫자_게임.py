# 7311
# 8622

def solution(A, B):
    A.sort(reverse = True)
    B.sort(reverse = True)
    
    # B의 요소가 A의 요소들을 이길 수 있는 최대 값을 구하는 과정
    pa = 0
    pb = 0
    answer = 0
    while pa < len(A) and pb < len(B):
        # a가 b보다 작다면
        if A[pa] < B[pb]:
            # answer, 포인터 업데이트
            answer += 1
            pa += 1
            pb += 1
        # a가 b보다 크다면
        else:
            # 다음 pa를 pb와 비교함
            pa += 1
            
    return answer