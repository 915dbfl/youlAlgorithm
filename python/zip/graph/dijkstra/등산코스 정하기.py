# 1시간 6분

# 문제 정리
# 양방향 통행
# 각 지점은 출입구, 쉼터, 산봉우리 중 하나
# 휴식 없이 이동해야 하는 시간 중 가장 긴 시간 -> intensity
# 출입구는 여러 개 -> 산봉우리 한 곳 방문 -> 다시 원래의 출입구로 돌아옴
# 출입구는 처음 / 끝, 산봉우리는 한 번만 포함되어야 함
# intensity 최소 등산 코스
# 등산코스 여러 개 -> 산봉우리 번호가 가장 낮은 코스 선택

# 제약 조건 정리
# 지점수 n <= 50_000
# path수 paths <= 200_000
# 이동하는 데 걸리는 시간 <= 10_000_000

"""
풀이법
1. 출입구 -> 산봉우리 dfs 진행
    1) 시작점은 gates 중 하나
    2) (산봉우리, intensity, 현재 위치) 저장
        - 초기값: (None, 0, 출입구)
    3) 산봉우리가 != None: // 등산로 완성
        - minintensity는 최소 intensity로 업데이트
        - intensity 업데이트에 따라 산봉우리 업데이트
    4) 가지치기 // 각 지점 최저 intensity와 비교
        - minintensity <= intensity 제거 
    5) 각 지점 최저 intensity 업데이트
    5) 다음 지점으로 이동
        - 최저 intensity 확인
        - 산봉우리일 경우
            - 산봉우리가 없어야 함
        - 단순 쉼터일 때 -> 추가
"""

# 해당 코드는 우선순위 큐를 사용하지 않았기 때문에 다익스트라가 아님
from collections import deque, defaultdict

def solution(n, paths, gates, summits):
    dq = deque()
    path_dict = defaultdict(list)
    
    min_intensity = 10**7 + 1
    top = -1
    
    # path 정보 저장
    for i, j, w in paths:
        path_dict[i].append((j, w))
        path_dict[j].append((i, w))
        
    # min_intensity
    min_intensities = [10**7+1] * (n+1)
    
    # 시작점 저장
    for gate in gates:
        dq.append((None, 0, gate))
        
    # 존재 여부를 파악할 때 효율을 높이기 위해 set으로 변경
    gates = set(gates)
    summits = set(summits)
        
    while dq:
        t, i, cur = dq.popleft()
        
        # 등산로 완성!
        if t != None:
            if min_intensity > i:
                min_intensity = i
                top = t
            elif min_intensity == i:
                top = min(top, t)
            continue
                
        # 가지치기
        if min_intensities[cur] <= i:
            continue
        
        min_intensities[cur] = i
        # 다음 지점으로 이동
        for nn, nw in path_dict[cur]:
            ni = max(i, nw)
            if ni > min_intensities[nn]: continue
            
            if nn in summits: # 산봉우리일 경우, 산봉우리가 없어야 함
                if t == None:
                    dq.append((nn, ni, nn))
            elif nn not in gates: # 단순 쉼터일 때
                dq.append((t, ni, nn))
                    
    return [top, min_intensity]

# 코드 최적화: 다익스트라 적용

from collections import defaultdict
from heapq import heappop, heappush

def solution(n, paths, gates, summits):
    def get_min_intensity():
        result = [0, 10**7+1]
        hq = []
        visited = [10**7+1] * (n + 1)

        # 출발지 우선순위 큐에 삽입
        for gate in gates:
            heappush(hq, (0, gate))
            visited[gate] = 0

        while hq:
            intensity, node = heappop(hq)

            # 산봉우리일 경우
            if node in summits_set:
                if result[1] > intensity:
                    result = [node, intensity]
                elif result[1] == intensity and result[0] > node:
                    result[0] = node
                continue
                
            # 가지치기
            if intensity > visited[node]:
                continue

            # 다음 위치로 이동
            for weight, next_node in graph[node]:
                new_intensity = max(intensity, weight)
                if new_intensity < visited[next_node]:
                    visited[next_node] = new_intensity
                    heappush(hq, (new_intensity, next_node))

        return result

    summits.sort()
    summits_set = set(summits)
    
    # 양방향 등산로 정보 저장
    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((w, j))
        graph[j].append((w, i))

    return get_min_intensity()