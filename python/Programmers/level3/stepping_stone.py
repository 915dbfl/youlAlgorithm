#22.07.25
#징검다리 건너기

#효율성 두 개 통과 못함
#시간복잡도 = stone 배열의 크기 * stone 배열의 크기 = 20만 * 20만
def solution(stones, k):
    m = 200000000
    size = len(stones)
    for i in range(size):
        tmp = 1
        if stones[i] >= m: 
            continue
            
        for l in range(i-1, max(-1, i-k), -1):
            if stones[i] >= stones[l]:
                tmp += 1
            else:
                break
                
        if len(stones)-i-1+tmp < k:
            continue
            
        for j in range(i+1, min(i+k, size)):
            if stones[i] >= stones[j]:
                tmp += 1
            else:
                break

        if tmp >= k:
            m = min(m, stones[i])
    return m

# 이분탐색
# 시간복잡도 = log(200000000) = 27-28
def solution(stones, k):
    start = 1
    end = max(stones)
    
    while start <= end:
        mid = (start+end)//2
        count = 0
        for i in stones:
            if count < k:
                if i-mid <= 0:
                    count += 1
                else:
                    count = 0
            else:
                break
        if count < k:
            start = mid+1
        else:
            end = mid-1
            result = mid
    return result