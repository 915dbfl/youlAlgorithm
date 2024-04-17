from collections import Counter

# O(n^2)
def solution(a):
    answer = -1
    
    numcnt = Counter(a)
    print(numcnt)
    
    # a에 있는 원소 k를 기준으로 스타 배열을 만들 수 있는지 검사
    for k in numcnt.keys():
        
        # 이미 구해진 answer보다 배열 속 k의 개수가 더 작은지 확인
        if numcnt[k] < answer: continue
        
        # k의 등장횟수 확인
        cnt = 0
        idx = 0
        while idx < len(a) - 1:
            # k가 포함되지 않거나 서로 값이 동일하면 스타배열 불가
            if (a[idx] != k and a[idx+1] != k) or (a[idx] == a[idx]+1):
                idx += 1
                continue
            
            # 스타 배열이 되는 경우 cnt 업데이트
            cnt += 1
            # 해당 두 값 다음을 확인하기 위해 두칸 점프
            idx += 2
            
        answer = max(cnt, answer)
        
    return answer*2 if answer != -1 else answer

def solution(a):
    answer = 0
    n = len(a)
    chk = [-1] * (n+2)
    a = [a[0]] + a + a[-1]