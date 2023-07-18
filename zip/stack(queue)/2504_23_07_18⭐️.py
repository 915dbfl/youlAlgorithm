#괄호의 값

#런타임 에러
# import sys
# bracket = list(input())
# wrong = False

# def cal(lst):
#     global wrong
#     tmp1 = tmp2 = 0
#     start = end = 0
#     formula = "0"

#     if wrong:
#         return
    
#     for i in range(len(lst)):
#         end = i
#         if lst[i] == "(":
#             tmp1 += 1
#         elif lst[i] == ")":
#             tmp1 -= 1
#         elif lst[i] == "[":
#             tmp2 += 1
#         elif lst[i] == "]":
#             tmp2 -= 1

#         if tmp1 < 0 or tmp2 < 0:
#             wrong = True
#             return
        
#         if tmp1 == 0 and tmp2 == 0:
#             type = "2" if lst[start] == "(" else "3"
#             if start + 1 >= end:
#                 formula += "+ " + type
#             else:
#                 formula += "+ " + type + " * (" + cal(lst[start+1:end]) + ")"
#             start = i+1
    
#     return formula
        

# result = cal(bracket)
# if wrong:
#     print(0)
# else:
#     print(eval(result))

#스택
bracket = list(input())

stack = []
answer = 0
tmp = 1

for i in range(len(bracket)):

    if bracket[i] == "(":
        stack.append(bracket[i])
        tmp *= 2

    elif bracket[i] == "[":
        stack.append(bracket[i])
        tmp *= 3

    elif bracket[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if bracket[i-1] == "(":
            answer += tmp
        stack.pop()
        tmp //= 2

    else:
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if bracket[i-1] == "[":
            answer += tmp

        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)