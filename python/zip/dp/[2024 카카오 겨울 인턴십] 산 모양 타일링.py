# 1시간 10분

def solution(n, tops):
    if tops[0] == 1:
        ans = 4
        pf = 3
    else:
        ans = 3
        pf = 2
        
    for i in range(1, n):
        cur = ans
        # 덮개가 있는 경우
        if tops[i] == 1:
            cur *= 3
            cur += pf 
            pf += ans * 2
        # 덮개가 없는 경우
        else:
            cur *= 2
            cur += pf
            pf += ans
        ans = cur % 10007
        
    return ans