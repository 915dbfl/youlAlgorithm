# 이진 트리를 만들 수 없는 경우
# 루트가 없는데 자식이 있을 때
# 루트와 자식의 idx 연관관계 구하기
# 포화 이진트리여야 하므로 이진 수의 길이는 무조건 짝수이어야 한다.
from collections import deque

# 이진수로 변환
def t2b(number):
    return bin(number)[2:]

# 포화 이진트리로 변환
# 10**15의 이진수 길이가 53이므로 그보다 큰 63까지만 확인
def make_full(b):
    full_cnt = [1, 3, 7, 15, 31, 63]
    l = len(b)
    
    for i in range(6):
        if l <= full_cnt[i]:
            return "0" * (full_cnt[i] - l) + b

# 루트와 자식들을 확인하며 표현 가능한 이진트리인지 확인
def check_child(b):
    dq = deque()
    des = ((len(b)+1)//2)//2
    dq.append(((len(b)+1)// 2, des))
    
    while dq:
        cur, d = dq.popleft()
        # 잎이 아닌 경우
        if cur % 2 == 0:
            if b[cur-1] == "0" and (b[cur - d -1] == "1" or b[cur + d - 1] == "1"):
                return False
        
            dq.append((cur-d, d//2))
            dq.append((cur+d, d//2))
    return True
    
def solution(numbers):
    answer = []
    
    # 각 숫자 이진수로 만들기
    for num in numbers:
        bi = make_full(t2b(num))
        if check_child(bi):
            answer.append(1)
        else:
            answer.append(0)
            
    return answer

# 다른 풀이
def dnc(num, left, right):
    if left == right:
        return [True, int(num[left])]

    mid = (left + right) // 2
    root = int(num[mid])

    left_subtree = dnc(num, left, mid - 1)
    right_subtree = dnc(num, mid + 1, right)

    flag = left_subtree[1] or right_subtree[1]

    if flag == 1 and root == 0:
        return [0, 0]

    return [left_subtree[0] and right_subtree[0], root]

def get_answer(num):
    
    # 최대 53번만 whil문이 실행됨
    tmp = ''
    while num > 0:
        tmp = tmp + str(num % 2)
        num //= 2
    # 0으로 패딩 채우기
    size = 1
    while len(tmp) > pow(2, size) - 1:
        size += 1
    while len(tmp) < pow(2, size) - 1:
        tmp += '0'

    return int(dnc(tmp, 0, len(tmp) - 1)[0])

def solution(numbers):
    answer = [get_answer(num) for num in numbers]
    return answer