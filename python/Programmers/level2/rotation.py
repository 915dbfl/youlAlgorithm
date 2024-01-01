#2022.03.18
#행렬 테두리 회전하기

#첫 풀이
def rotation(i):
    x1, y1, x2, y2 = i
    changes = []
    tmp = lst[x1-1][y1-1]
    old = 0
    for i in range(y1, y2):
        old = lst[x1-1][i]
        changes.append(old)
        lst[x1-1][i] = tmp
        tmp = old
    for i in range(x1, x2):
        old = lst[i][y2-1]
        changes.append(old)
        lst[i][y2-1] = tmp
        tmp = old
    for i in range(y2-1, y1-1, -1):
        old = lst[x2-1][i-1]
        changes.append(old)
        lst[x2-1][i-1] = tmp
        tmp = old
    for i in range(x2-1, x1-1, -1):
        old = lst[i-1][y1-1]
        changes.append(old)
        lst[i-1][y1-1] = tmp
        tmp = old
    return min(changes)


def solution(rows, columns, queries):
    global lst 
    answer = []
    lst =[[x for x in range((k*columns+1),(k*columns+columns+1))]for k in range(rows)]

    for i in queries:
        answer.append(rotation(i))

    return answer

#두 번째 풀이: old, new 변수를 두는 대신 changes에 저장된 값을 사용!
#더 나은 방법
def rotation(i):
    x1, y1, x2, y2 = i
    stack = [lst[x1-1][y1-1]]
    for i in range(y1, y2):
        stack.append(lst[x1-1][i])
        lst[x1-1][i] = stack[-2]
    for i in range(x1, x2):
        stack.append(lst[i][y2-1])
        lst[i][y2-1] = stack[-2]
    for i in range(y2-1, y1-1, -1):
        stack.append(lst[x2-1][i-1])
        lst[x2-1][i-1] = stack[-2]
    for i in range(x2-1, x1-1, -1):
        stack.append(lst[i-1][y1-1])
        lst[i-1][y1-1] = stack[-2]
    return min(stack)
        
    
def solution(rows, columns, queries):
    global lst 
    answer = []
    lst =[[x for x in range((k*columns+1),(k*columns+columns+1))]for k in range(rows)]

    for i in queries:
        answer.append(rotation(i))
        
    return answer