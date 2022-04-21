#22.04.2
#주식 가격

#내 풀이
def solution(prices):
    l = len(prices)
    answer = [0 for i in range(l)]
    stack = [l-1]
    for i in range(l-2, -1, -1):
        cnt = 0
        while stack:
            tmp = stack[-1]
            if prices[i] <= prices[tmp]:
                answer[i] += answer[tmp]
                stack.pop()
            else:
                break
        answer[i] += 1
        stack.append(i)
    return answer