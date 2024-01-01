#22.05.20
#이중우선순위큐

#내 풀이: heapq 사용
import heapq

def solution(operations):
    heap = []
    for i in operations:
        op, val = i.split(" ")
        if op == "I":
            heapq.heappush(heap, int(val))
        elif len(heap) > 0 and val == "-1":
            heapq.heappop(heap)
        elif len(heap)> 0  and val == "1":
            if len(heap) == 1:
                heap.pop()
            else:
                #최대값이 마지막 두 원소 안에 들어있지 않을 수도 있으므로 해당 풀이는 틀린 풀이이다.
                a = heap[-1]
                b = heap[-2]
                if a>b: heap.pop(-1)
                else: heap.pop(-2)
            heapq.heapify(heap)
            
    return [0,0] if len(heap) == 0 else [max(heap[-1], heap[-2]), heap[0]]


# 다른 풀이: 두개의 heap 사용
from heapq import heappush, heappop, heapify

def solution(arguments):
    max_heap = []
    min_heap = []
    for i in arguments:
        op, val = i.split(" ")
        if op == "I":
            heappush(max_heap, -int(val))
            heappush(min_heap, int(val))
        elif op == "D":
            try:
                if val == "1":
                    min_heap.remove(-max_heap[0])
                    heapify(min_heap)
                    heappop(max_heap)
                else:
                    max_heap.remove(-min_heap[0])
                    heapify(max_heap)
                    heappop(min_heap)
            except:
                continue
    if len(max_heap) == 0:
        return [0, 0]
    else:
        return [-heappop(max_heap), heappop(min_heap)]