"""
[풀이 과정] - 오답
1. 취약 지점을 다 돌 수 있는 가장 짧은 루트 구하기 -> ⭐️ 무조건 해당 루트가 정답은 아님!!
2. 최소 인원 구하기
    - dist 순으로 작업? -> 최선의 답이 아님
    - dist 순열 구하기 -> 모든 경우 확인
"""
from itertools import permutations
import sys

def is_not_finished(s, e, dir):
    return (dir == 1 and s < e) or (dir == -1 and s > e)

def get_min_worker(n, start, end, dir, dist, weak):
    worker_idx = 0
    if dir == 1 and start > end: # 시계 방향일 때
        end += n
    elif dir == -1 and start < end:
        start += n
    
    while is_not_finished(start, end, dir):
        # 취약 지점을 모두 돌 수 없는 경우
        if worker_idx >= len(dist):
            return -1
        
        if abs(end - start) > dist[worker_idx]:
            start += dir * dist[worker_idx]
            worker_idx += 1
        elif abs(end - start) <= dist[worker_idx]:
            return worker_idx + 1
        
        while start not in weak:
            if (dir == 1 and start >= end) or (dir == -1 and start <= end):
                return worker_idx
            start += dir
            
    return worker_idx + 1
            
def get_best_route(n, weak, dist):
    route_s = -1
    route_e = -1
    route_d = n+1
    dir = 0
    weak_size = len(weak)
    
    for i in range(weak_size):
        # 시계 방향 루트
        cs = i
        ce = (i+1) % weak_size
        
        if ce < cs:
            route1 = n - (weak[ce] + n - weak[cs])
        else:
            route1 = n - (weak[ce] - weak[cs])
            
        # 반시계 방향 루트
        rcs = i
        rce = (i-1+weak_size)% weak_size
        if rce > rcs:
            route2 = n - (weak[rcs] + n - weak[rce])
        else:
            route2 = n - (weak[rcs] - weak[rce])
        
        # 두 루트 비교 후 업데이트
        if route1 > route2: 
            if route_d > route2:
                route_d = route2
                route_s = weak[rcs]
                route_e = weak[rce]
                dir = 1
        else: # 시계가 더 유리
            if route_d > route1:
                route_d = route1
                route_s = weak[cs]
                route_e = weak[ce]
                dir = -1
                
    return [route_s, route_e, dir]
    
def solution(n, weak, dist):
    s, e, dir = get_best_route(n, weak, dist)
    
    min_worker = sys.maxsize
    for case in permutations(dist):
        case_worker = get_min_worker(n, s, e, dir, case, weak)
        if case_worker != -1 and min_worker > case_worker:
            min_worker = case_worker
    return -1 if min_worker == sys.maxsize else min_worker

"""
[재풀이]
1. 시작 취약 지점 구하기
2. 작업자 순열 구하기
3. 취약 지점 전체 돌기 -> 최소 투입 인원 구하기
"""

from itertools import permutations
import sys

def solution(n, weak, dist):
    weak_len = len(weak)
    dist.sort(reverse = True)
    extended_weak = weak + [n + w for w in weak]
    min_workers = sys.maxsize
    
    for start in range(weak_len):
        for case in permutations(dist):
            workers = 0
            position = extended_weak[start]
            # 취약 지점 전체 돌기
            for i in range(weak_len):
                next_weak = extended_weak[start + i]
                diff = next_weak - position
                if diff > case[workers]:
                    workers += 1
                    if workers >= len(dist):
                        break
                    position = next_weak
            else:
                 min_workers = min(min_workers, workers+1) 
    return min_workers if min_workers != sys.maxsize else -1