# 오름차순으로 정렬 후 return
# 존재하지 않을 경우 [-1] return
# 1<=n<=10000

def solution(n, s):
    if n > s:
        return [-1]
    else:
        base = s // n
        answer = [base] * n
        
        if base * n < s:
            sum = base * n
            idx = n-1
            while sum < s:
                answer[idx] += 1
                sum += 1
                idx -= 1
                
        return answer
    
# s//n인 a를 몫만큼, (a+1)을 나머지만큼 진행하는 방식도 존재
                