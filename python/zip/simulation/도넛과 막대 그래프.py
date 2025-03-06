# 30분

"""
# 주요 정보
- 도넛 - n개의 정점과 간선
- 막대 - n개의 정점과 n-1개의 간선
- 8자 모양 - 2n+1개의 정점 / 2n+2개의 간선
    - 크키가 동일한 2개의 도넛 모양 그래프에서 두개의 정점을 결합한 형태
    
# 생성 정점 / 각 그래프 개수
- 생성한 정점에서 다른 그래프로 뻗어나감
    - indegree가 0인 경우 파악
    - 막대일 시작도 indegree가 0
    - out_degree가 막대는 무조건 1개, 루트는 2개 이상이다.(조건에서 그래프는 2개 이상이라 했으므로)
- 부모를 파악했을 때 가장 상위가 생성 정점이 됨
    - 다음 순으로 bfs 진행을 한다.
    - in_degree == 2 & out_degree == 2인 노드를 지난다면? -> 8자
    - 재방문하는 노드가 있다면 -> 도넛
    - 리프에 도달했을 때 -> 막대
"""
from collections import defaultdict, deque

def solution(edges):
    in_degree = defaultdict(list)
    out_degree = defaultdict(list)
    nodes = []
    visited = set()
    
    # degree 기록
    for start, end in edges:
        in_degree[end].append(start)
        out_degree[start].append(end)
        nodes.append(start)
        nodes.append(end)
      
    # 루트 찾기
    root = -1
    for node in list(nodes):
        if len(in_degree[node]) == 0 and len(out_degree[node]) >= 2:
            root = node
            break
            
    dq = deque()
    # 생성 정점 번호, 도넛, 막대, 8자 개수
    donut = 0
    stick = 0
    eight = 0
    # 루트에서 dfs 진행
    for nxt in out_degree[root]:
        dq.append(nxt)
        visited.add(nxt)
        
    while dq:
        cur = dq.popleft()
        
        # 8자 파악 -> 더 이상 방문하지 않음
        if len(in_degree[cur]) >= 2 and len(out_degree[cur]) >= 2:
            eight += 1
            continue
        
        stick_flag = True
        for nxt in out_degree[cur]:
            if nxt not in visited:
                stick_flag = False
                visited.add(nxt)
                dq.append(nxt)
            else:
                donut += 1
                stick_flag = False
                break

        if stick_flag:
            stick += 1
    
    return [root, donut, stick, eight]

# 조금 더 깔끔한 풀이
def solution(edges):
    answer = [0, 0, -1, 0]
    total = 0

    n = 0
    for a, b in edges:
        n = max(n, a, b)
        
    # 노드 in / out 수        
    meta = [[0, 0] for _ in range(n+1)]
    graph = [0] * (n+1)
    for a, b in edges:
        graph[a] += 1
        meta[b][0] += 1
        meta[a][1] += 1
    
    total = 0
    for num, (in_num, out_num) in enumerate(meta):
        # root 정점 파악 / 그래프 total 초기화
        if in_num == 0 and out_num >= 2:
            answer[0] = num
            total = graph[num]
           
        # 막대 그래프 확인
        if in_num >= 0 and out_num == 0:
            answer[2] += 1
            
        # 8 그래프 확인
        if in_num >= 2 and out_num == 2:
            answer[3] += 1
            
    answer[1] = total - answer[2] - answer[3]
    return answer
            