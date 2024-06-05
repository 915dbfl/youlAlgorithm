# 20분
def solution(n, t, m, p):
    num = 0
    base, answer = "", ""
    case = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    
    def getNum(num, n):
        result = ""
        while num >= n:
            result += case[num % n]
            num = num // n
            
        result += case[num]
        
        return result[::-1]
    
    while len(base) < (t*m):
        base += getNum(num, n)
        num += 1
        
    pointer = p-1
    # while len(answer) < t:
    #     answer += base[pointer]
    #     pointer += m
        
    # return answer

    return base[p-1::m][:t]