#22.07.25
#징검다리 건너기

#효율성 두 개 통과 못함
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