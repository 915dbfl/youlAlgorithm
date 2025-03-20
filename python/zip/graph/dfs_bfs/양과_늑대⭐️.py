# 23분
from collections import defaultdict, deque

def solution(info, edges):
    cnt = len(info)
    graph = defaultdict(list)
    
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    dq = deque()
    # 현재 노드, 양 수, 늑대 수
    dq.append((set([0]), 1, 0))
    
    answer = 0
    while dq:
        group, sheep, wolve = dq.popleft()
        answer = max(sheep, answer)
        
        # 가능한 모든 간선 확인
        for cur in group:
            for nxt in graph[cur]:
                # 방문하지 않았고
                if nxt not in group:
                    nsh = sheep
                    nw = wolve
                
                    # 양 / 늑대의 정보 업데이트
                    if info[nxt] == 1:
                        nw += 1
                    else:
                        nsh += 1

                    # 잡아 먹히지 않을 경우
                    if nsh > nw:
                        new_set = group | set([nxt])
                        dq.append((new_set, nsh, nw))

    return answer

# dfs + backtracking
# 양방향 경로더라도 불필요하다면 단방향 도로로 생각하기
# 재풀이 / 35분

def solution(info, edges):
    answer = 0
    # 방분 여부 확인
    visited = [False] * len(info)
    
    def dfs(nsheep, nwolf):
        nonlocal answer
        answer = max(answer, nsheep)
        
        for s, e in edges:
            # 다음으로 방문이 가능한지 확인
            if visited[s] and not visited[e]:
                new_nsheep = nsheep if info[e] else nsheep + 1
                new_nwolf = nwolf + 1 if info[e] else nwolf
                
                # 양이 잡아 먹히지 않는 경우인가?
                if new_nsheep > new_nwolf:    
                    visited[e] = True
                    dfs(new_nsheep, new_nwolf)
                    visited[e] = False

    # dfs 진행
    visited[0] = True
    dfs(1, 0)
    
    return answer
    

# 방문 가능한 노드 저장 풀이
def solution(info, edges):
    answer = 0
    # 갈 수 있는 다음 노드를 나타냄
    nxt_nodes = set()
    # 방분 여부 확인
    visited = [False] * len(info)
    
    def dfs(cur_node, nsheep, nwolf, nxt_nodes):
        nonlocal answer
        answer = max(answer, nsheep)
        
        for nxt in nxt_nodes:
            new_nsheep = nsheep if info[nxt] else nsheep + 1
            new_nwolf = nwolf + 1 if info[nxt] else nwolf
            
            if new_nsheep > new_nwolf:
                visited[nxt] = True
                nxt_next_nodes = set(nxt_nodes) - set([nxt])
                for s, e in edges:
                    if visited[s] and not visited[e]:
                        nxt_next_nodes.add(e)
                        
                dfs(s, new_nsheep, new_nwolf, nxt_next_nodes)
                visited[nxt] = False

        for s, e in edges:
            # 한 번도 방문하지 않은 다음 방문 노드 정하기
            nxt = -1
            if visited[e] and not visited[s] and s in nxt_nodes:
                nxt = s
            elif visited[s] and not visited[e] and e in nxt_nodes:
                nxt = e

            # 다음 노드 방문
            if nxt != -1:
                new_nsheep = nsheep if info[nxt] else nsheep + 1
                new_nwolf = nwolf + 1 if info[nxt] else nwolf

    # 루트에 따른 다음 방문 가능한 노드들 추가
    visited[0] = True
    for s, e in edges:
        if s == 0:
            nxt_nodes.add(e)
        elif e == 0:
            nxt_nodes.add(e)
            
    # dfs 진행
    dfs(0, 1, 0, nxt_nodes)
    return answer
    