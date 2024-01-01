# 매 단계에서 음식 시간이 가장 작은 음식을 선택한다. - 그리디
# 음식 시간이 가장 작은 것을 선택하므로 최소 힙 사용

import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k크거나 같다면 -1
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1)) # (음식 시간, 음식 번호)

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식의 개수

    while sum_value + (q[0][0] - previous) * length <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key = lambda x : x[1]) # 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]