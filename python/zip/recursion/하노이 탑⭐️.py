# 오답
# 탑다운, 재귀
from collections import deque
answer = []
tops = [deque(), deque(), deque()]

# target에 level짜리 탑을 쌓는 경우
def make_top(target, tmp, level):
    # 1을 쌓는 경우
    if level == 1:
        if tops[(target+1)%3] and tops[(target+1)%3][0] == 1:
            nxt_target = (target+1)%3
        else:
            nxt_target = (target+2)%3
        tops[nxt_target].popleft()
        tops[target].appendleft(1)
        answer.append([nxt_target, target])
        return
    
    make_top(tmp, target, level-1)
    if tops[(target+1)%3] and tops[(target+1)%3][0] == level:
        nxt_target = (target+1)%3
    else:
        nxt_target = (target+2)%3
    tops[nxt_target].popleft()
    tops[target].appendleft(level)
    answer.append([nxt_target, target])
    make_top(target, nxt_target, level-1)
    
def solution(n):
    # 초기탑 채우기
    for i in range(1, n+1):
        tops[0].appendleft(i)
    
    make_top(3, 2, n)
    
    return answer

# 재귀 정답
def solution(n):
    answer = []
    
    def hanoi(n, str, end, mid):
        if n == 1:
            answer.append([str, end])
        else:
            hanoi(n-1, str, mid, end)
            answer.append([str, end])
            hanoi(n-1, mid, end, str)
            
    hanoi(n, 1, 3, 2)
    return answer