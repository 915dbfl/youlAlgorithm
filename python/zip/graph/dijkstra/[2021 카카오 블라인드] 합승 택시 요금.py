# 다익스트라 사용
from heapq import heappush, heappop
from collections import defaultdict
import sys
INF = sys.maxsize

def dijkstra(n, start, dic):
    visited = [INF] * (n+1)
    visited[start] = 0
    
    hq = []
    heappush(hq, (0, start))
    
    while hq:
        cost, cur = heappop(hq)
        
        if cost > visited[cur]:
            continue
            
        for c, nxt in dic[cur]:
            if visited[nxt] > cost + c:
                visited[nxt] = cost + c
                hq.append((cost + c, nxt))
                
    return visited

def solution(n, s, a, b, fares):
    dic = defaultdict(list)
    
    for c, d, f in fares:
        dic[c].append((f, d))
        dic[d].append((f, c))
        
    start = dijkstra(n, s, dic)
    a = dijkstra(n, a, dic)
    b = dijkstra(n, b, dic)
    
    answer = INF
    for i in range(1, n+1):
        answer = min(answer, start[i] + a[i] + b[i])
        
    return answer
    
# 플로이드 워샬 활용
import sys
INF = sys.maxsize

def solution(n, s, a, b, fares):
    dist = [[INF] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        dist[i][i] = 0
        
    for x, y, c in fares:
        dist[x][y] = c
        dist[y][x] = c
        
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    answer = INF
    for i in range(1, n+1):
        answer = min(answer, dist[s][i]+dist[i][a]+dist[i][b])
    return answer