#22.04.09
#지나가는 트럭

#내 풀이
from collections import deque

def solution(bridge_length, weight, truck_weights):
    dq = deque()
    dq.append([truck_weights[0],0])
    idx = 1
    answer = 0
    while idx < len(truck_weights):
        answer += 1
        if answer - dq[0][1] == bridge_length:
            dq.popleft()  
        if sum([x[0] for x in dq]) + truck_weights[idx] <= weight:
            dq.append([truck_weights[idx], answer])
            idx += 1

    return answer + bridge_length + 1 if answer != 0 else bridge_length + 1