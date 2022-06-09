#22.06.09
#배달

#내 풀이(32번 시간초과): bfs 풀이
from collections import deque
import sys
sys.setrecursionlimit(10**3)

def dfs(cur, lst, k):
    global l, graph, answer, limit
    if len(lst) == l:
        return
    for i in graph[cur].keys():
        if i not in lst and k+graph[cur][i] <= limit:
            answer.add(i)
            dfs(i, lst+[i], k+graph[cur][i])

def solution(N, road, K):
    global graph, answer, l, limit
    l = N
    limit = K
    graph = [{} for _ in range(N+1)]
    for a, b, c in road:
        if b in graph[a].keys():
            graph[a][b] = min(graph[a][b], c)
            graph[b][a] = min(graph[b][a], c)
        else:
            graph[a][b] = c
            graph[b][a] = c
        
    answer = set([1])
    dfs(1, [1], 0)
    return len(answer)