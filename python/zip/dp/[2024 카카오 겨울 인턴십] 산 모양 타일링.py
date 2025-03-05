# 30분

def solution(n, tops):
    dp = []
    if tops[0] == 1:
        dp.extend([1, 4])
    else:
        dp.extend([1, 3])
        
    for i in range(1, n):
        if tops[i] == 1:
            dp.append((dp[-1] * 3 + dp[-1] - dp[-2]) % 10007)
        else:
            dp.append((dp[-1] * 2 + dp[-1] - dp[-2]) % 10007)
            
    return dp[-1]