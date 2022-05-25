#22.05.25
#가장 먼 노드

# 내 풀이 : bfs 사용
from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n+1)] # 간선 정보 저장
    chk = [0 for _ in range(n+1)]  # 하나로 연결된 선 정보 저장
    answer = [0 for _ in range(n+1)] # 각 노드의 최단경로 저장
    chk[0], chk[1], answer[1] = 1, 1, 1
    dq = deque([1]) # 탐색할 노드를 순서대로 저장
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    while dq:
        t = dq.popleft()
        for i in graph[t]:
            if chk[i] == 0:
                answer[i] = answer[t]+1
                dq.append(i)
                chk[i] = 1
                
    return answer.count(max(answer))