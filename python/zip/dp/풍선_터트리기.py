import sys
INF = sys.maxsize

def solution(a):
    l = len(a)

    # 각 위치에서 가장 작은 친구 구하기 -> O(2n)
    Min = [INF] * l
    Min[0] = a[0]
    for i in range(1, l):
        Min[i] = min(a[i], Min[i-1])
        
    Min_R = [INF] * l
    Min_R[-1] = a[-1]
    for i in range(l-2, -1, -1):
        Min_R[i] = min(a[i], Min_R[i+1])

    # target을 기준으로 양쪽의 최소값이
    # target보다 작을 경우 answer += 1
    answer = 2
    for i in range(1, l-1):
        target = a[i]
        if (Min[i-1] > target) or (Min_R[i+1] > target):
            answer += 1
            
    return answer