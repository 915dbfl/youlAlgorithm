#22.07.21
#여행경로

# 내 풀이(가능한 모든 경로를 구하는 과정에서 많은 시간이 든다.)
from collections import defaultdict

def dfs(dic, cur, route, visited):
    global answer, l
    if len(visited) == l:
        answer.append(route)
        return
    if cur not in dic:
        return
    else:
        for des in dic[cur]:
            if [cur, des] not in visited or visited.count([cur, des]) < dic[cur].count(des) :
                dfs(dic, des, route + [des], visited + [[cur, des]])
    
def solution(tickets):
    global answer, l
    answer = []
    l = len(tickets)
    dic = defaultdict(list)
    for s, e in tickets:
        dic[s].append(e)
        
    dfs(dic, "ICN", ["ICN"], [])
    answer.sort()
    return answer[0]

# 베스트 풀이: dfs 재귀 구현
from collections import defaultdict

def dfs(graph, N, cur, route):
    if len(route) == N+1:
        return route
    
    for idx, country in enumerate(graph[cur]):
      # 🔔다녀간 경로를 제거하고 하나의 경로가 끝난 후 다시 추가하는 방식을 이해하고 넘어가자!
        graph[cur].pop(idx)
        result = dfs(graph, N, country, route + [country])
        graph[cur].insert(idx, country)
        
        if result: # 미리 정렬을 했으므로 가장 처음 얻어지는 값이 정답이다.
            return result

def solution(tickets):
    graph = defaultdict(list)
    N = len(tickets)
    
    for s, e in tickets:
        graph[s].append(e)
        # 알파벳 순서가 앞서는 경로를 택하므로 미리 정렬을 진행한다.
        graph[s].sort()
    
    return dfs(graph, N, "ICN", ["ICN"])

# best 풀이: dfs 반복문 구현
from collections import defaultdict, deque

def solution(tickets):
    graph = defaultdict(list)
    for s, e in tickets:
        graph[s].append(e)
    for k in graph.keys():
        graph[k].sort()
        
    s = deque(["ICN"])
    p = []
    
    while s:
        cur = s[-1]
        if graph[cur] != []:
            s.append(graph[cur].pop(0))
        else:
            p.append(s.pop())
    return p[::-1]
