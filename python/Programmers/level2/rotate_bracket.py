#2022.04.07
#괄호 회전하기

def checkRight(s):
    while 1:
        if "[]" in s:
            s = s.replace("[]", "")
        elif "()" in s:
            s = s.replace("()", "")
        elif "{}" in s:
            s = s.replace("{}", "")
        else:
            break
    if len(s) == 0:
        return True
    else:
        return False
    
def solution(s):
    answer = 0
    for i in range(len(s)):
        answer += checkRight(s[i:]+s[:i])
    return answer