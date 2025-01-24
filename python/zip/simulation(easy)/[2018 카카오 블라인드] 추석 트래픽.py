"""
1시간 반
풀이과정 - 누적합
1. 소수점을 어떻게 처리 해야 할까?
    - 하나하나 다 다루면 양이 너무 많아진다.
    - 오름차순으로 정렬 (시작 - 도착)
2. 누적합으로 최대 처리 개수 구하기
"""

from collections import defaultdict

def get_time(time_str):
    h, m, s = time_str.split(":")
    h = int(h)
    m = int(m)
    s = float(s)
    return (h * 3600) + (m * 60) + s

def solution(lines):
    dic = defaultdict(int)
    # 시작 시간, 도착 시간 dictionary에 넣기
    for line in lines:
        _, end_time, duration = line.split()
        end = get_time(end_time)
        start = end - float(duration[:-1]) + 0.001
        dic[start] += 1
        # 끝시간 포함을 위해 1을 더함
        dic[end+1] -= 1
        
    # 시간 오름차순 정렬
    times = sorted(list(dic.keys()))
    
    # 누적합 배열 초기화
    prefix = [0] * len(times)
    prefix[0] = dic[times[0]]
    
    # 누적합 계산
    for i in range(1, len(times)):
        target_time = times[i]
        prefix_val = dic[target_time]
        prefix[i] += prefix[i-1] + prefix_val
        
    return 1 if len(times) == 1 else max(prefix)