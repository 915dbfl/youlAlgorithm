# intensity가 가장 낮은 등산 코스를 구하자
# 등산 코스 여러 개 -> 산봉우리가 가장 낮은 코스 선택
# 모든 경우 파악
    # 출발 지점과 산봉우리는 무조건 하나씩 존재해야 함
    # 방문 노드 체크: 굳이 방문했던 노드 다시 방문할 필요 없음.
        # 돌아가는 경우는 체크하지 않아도 됨.

# 일부 테스트 케이스 시간 초과
# gate의 개수에 따라 시간 복잡도 늘어남 => o(n * gate의 수)

from collections import defaultdict, deque

def bfs(gate, summit, dic):
    dq = deque()
    answer = [-1, 10000001] # 산봉우리 번호, 최소 강도
    min_dis = [10000001] * len(gate) # 각 위치 방문 최소 강도
    
    # 시작점 모두 넣어주기
    for i in range(len(gate)):
        if gate[i] == 1:
            min_dis[i] = 0
            dq.append((i, i, 0, set([i]))) # 현재 위치, 출발 지점, intensity, 방문 정보 저장
            
    while dq:
        cur, start, mxi, visited_info = dq.popleft()
            
        # mxi가 answer보다 클 경우 제외
        if mxi > answer[1] or min_dis[cur] < mxi:
            continue
            
        for w, j in dic[cur]:
            # 출발 지점(동일, 다른 출발 지점 모두 포함)을 여러 번 방문하는 경우
            # 이미 방문한 노드일 경우,
            # 강도가 이미 구해진 최소 강도보다 클 경우,
            # 해당 위치 방문 최소 강도 보다 강도가 클 경우 제외
            tmp_int = mxi if mxi > w else w
            if gate[j] == 1 or j in visited_info or tmp_int > answer[1] or min_dis[j] < tmp_int:
                continue
            
            # 산봉우리 방문할 경우
            if summit[j] == 1:
                # 강도가 더 작을 경우
                if tmp_int < answer[1]:
                    answer = [j, tmp_int]
                # 강도가 동일 할 경우, 산봉우리 번호가 더 낮은 곳 선택
                elif tmp_int == answer[1]:
                    if j < answer[0]:
                        answer[0] = j
                continue
            
            dq.append((j, start, tmp_int, visited_info | set([j])))
        
    return answer
    
def solution(n, paths, gates, summits):
    dic = defaultdict(list)
    
    # gate 배열에 0, 1로 저장
    gate = [0] * (n+1)
    for g in gates:
        gate[g] = 1
        
    # 산봉우리 배열에 0, 1로 저장
    summit = [0] * (n+1)
    for s in summits:
        summit[s] = 1
    
    # path dictionary에 저장
    for i, j, w in paths:
        dic[i].append((w, j))
        dic[j].append((w, i))
    
    # bfs 진행
    return bfs(gate, summit, dic)

# 다익스트라 활용
# 시작점이 다 다르지만, 결국 특정 위치까지의 최소 intensity만 구하면 되므로 다익스트라 활용 가능

from heapq import heappush, heappop
from collections import defaultdict

def dijkstra(n, dic, gates, summits):
    hq = []
    intensity = [10000001] * (n+1)
    
    for gate in gates:
        heappush(hq, (0, gate)) # 최대 강도, 현재 위치
        
    while hq:
        it, cur = heappop(hq)
        
        # 이전에 구해진 최소 강도가 it보다 작을 경우
        if intensity[cur] < it:
            continue
        
        # 산봉우리 방문을 완료한 경우
        if cur in summits:
            continue
            
        for w, j in dic[cur]:
            mxi = max(it, w)
            # 출발 지점이 아닐 경우, 해당 위치 최소 강도 업데이트
            if intensity[j] > mxi and j not in gates:
                intensity[j] = mxi
                heappush(hq, (mxi, j))
    
    # w <= 10000000이므로 최대 값은 10000001로 설정
    answer = [-1, 10000001]
    for summit in summits:
        if intensity[summit] < answer[1]:
            answer = [summit, intensity[summit]]
        elif intensity[summit] == answer[1]:
            if answer[0] > summit:
                answer[0] = summit
        
    return answer

def solution(n, paths, gates, summits):

    gates = set(gates)
    summits = set(summits)
    
    dic = defaultdict(list)
    for i, j, w in paths:
        dic[i].append((w, j))
        dic[j].append((w, i))
    
    return dijkstra(n, dic, gates, summits)