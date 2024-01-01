# 22.09.22
# level2
# 더 맵게
# 반복문을 돌 때마다 가장 맵지 않은 음식 두 개를 선택해야 한다.
# 최소힙을 사용해 가장 작은 수를 빠르게 찾는다.

# 내 풀이
from heapq import heapify, heappop, heappush

def solution(scoville, K):
    answer = 0
    heapify(scoville)

    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        heappush(scoville, heappop(scoville) + heappop(scoville) * 2)
        answer += 1

    return answer

# 추가사항
# heappushpop(heap, item): item을 푸시한 후, 가장 작은 항목을 팝!