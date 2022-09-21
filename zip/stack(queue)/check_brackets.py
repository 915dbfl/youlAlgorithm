# 22.09.21
# level2
# 올바른 괄호

# 삼항 연산자 사용
def solution(s):
    check = 0
    
    for i in s:
        check = check-1 if i == ")" else check+1
        if check <= -1:
            return False
    
    return check == 0

# 예외 처리 부분 눈에 익히기
def solution(s):
    check = []
    
    for i in s:
        if i == "(":
            check.append(i)
        else:
            try:
                check.pop()
            except IndexError:
                return False       
            
    return check == []