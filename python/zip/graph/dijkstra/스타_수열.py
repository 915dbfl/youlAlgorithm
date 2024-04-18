# 오답
# 특정 교집합을 중심으로 구한 게 아니기 때문에
# idx를 증가시키는 과정에서 놓치는 부분이 있다 생각!
from collections import defaultdict

def getStar(a, start):
    # 스타 수열이 될 수 있는 후보
    star = defaultdict(int)
    idx = start
    
    while idx < len(a):
        # 서로 다른 수라면
        if a[idx] != a[idx-1]:
            # 스타 수열 후보에 추가
            star[a[idx]] += 1
            star[a[idx-1]] += 1
            # 두개값 건너뜀
            idx += 2
        else:
            idx += 1
    return star

def getMax(dic):
    global answer
    # 스타 수열의 교집합이 될 수 있는 값을 중심으로
    # 최대 스타 수열의 길이를 구하자
    for key in dic:
        answer = max(answer, dic[key]*2)

def solution(a):
    global answer
    answer = 0
    result = getStar(a, 1)
    getMax(result)
    
    result = getStar(a, 2)
    getMax(result)

    return answer

# 각 교집합이 될 수 있는 값에 대한
# 스타수열의 최대 길이를 구해야 함
from collections import Counter

def solution(a):
    star = Counter(a)
    answer = 0
    
    for key in star:
        # 최대 교집합의 수보다 적으면 continue
        if star[key] < answer:
            continue
        
        cnt = 0
        idx = 1
        while idx < len(a):
            if (a[idx] != key and a[idx-1] != key) or (a[idx] == a[idx-1]):
                idx += 1
                continue
                
            cnt += 1
            idx += 2
            
        answer = max(answer, cnt)
        
    return answer*2