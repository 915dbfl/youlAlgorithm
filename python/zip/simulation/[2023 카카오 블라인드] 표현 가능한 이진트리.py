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

# 다른 풀이
def checkTree(binary_num):
    # 리프 노드일 경우
    if len(binary_num) == 1:
        return (True, binary_num == "1")
    
    # 루트 확인
    route_idx = len(binary_num) // 2
    lr, lv= checkTree(binary_num[:route_idx])
    rr, rv = checkTree(binary_num[route_idx + 1:])
    
    # 루트가 없는 경우
    if binary_num[route_idx] == '0':
        # 하위 트리에 1이 아예 없어야 함
        if not lv and not rv and lr and rr:
            return (True, lv | rv)
        else:
            return (False, lv | rv)
    # 루트가 있는 경우
    else:
        # 하위 트리가 모두 정상 트리여야 함
        if lr and rr:
            return (True, True)
        else:
            return (False, True)
            
def getBinary(num):
    result = ""
    
    # 이진수 구하기
    while num >= 2:
        result += str(num % 2)
        num //= 2
    result += str(num)
    
    return result[::-1]
import math

def getMinTotalNodeCnt(num):
    pow_num = int(math.log(len(num), 2))
    return 2 ** (pow_num + 1) - 1

def solution(numbers):
    result = []
    for num in numbers:
        binary_num = getBinary(num)
        
        # 포화 이진트리 만들기
        min_total_node = getMinTotalNodeCnt(binary_num)
        left_node = min_total_node - len(binary_num)
        binary_num = '0' * left_node + binary_num
            
        # 결과 추가하기
        tr, _ = checkTree(binary_num)
        result.append(1 if tr else 0)
        
    return result   

# depth를 이요한 풀이
import math

def dfs(b, i, depth):
    if depth == 0:
        return True
    
    if b[i] == '0':
        if b[i - depth] == '1' or b[i + depth] == '1':
            return False
        
    left = dfs(b, i - depth, depth // 2)
    right = dfs(b, i + depth, depth // 2)
    return left and right

def solution(numbers):
    answer = []
    for num in numbers:
        b = bin(num)[2:]
        h = math.ceil(math.log2(len(b) + 1))
        size = 2**h - 1
        dummy = size - len(b)
        b = '0' * dummy + b
            
        result = dfs(b, len(b)//2, (len(b) + 1)//4)
        answer.append(1 if result else 0)
        
    return answer