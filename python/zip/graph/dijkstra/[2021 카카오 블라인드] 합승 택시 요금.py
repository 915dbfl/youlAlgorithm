# 다익스트라 사용
# 23분

import sys
from heapq import heappush, heappop
from collections import defaultdict

def solution(n, s, a, b, fares):
    edges = defaultdict(list)
    
    for start, end, cost in fares:
        edges[start].append((cost, end))
        edges[end].append((cost, start))
    
    def dijkstra(start):
        hq = []
        heappush(hq, (0, start))
        dist = [sys.maxsize] * (n+1)
        dist[start] = 0
        
        while hq:
            cur_cost, cur_node = heappop(hq)
            
            if dist[cur_node] < cur_cost:
                continue
                
            for nxt_cost, nxt_node in edges[cur_node]:
                if nxt_cost + cur_cost < dist[nxt_node]:
                    updated_cost = nxt_cost + cur_cost
                    dist[nxt_node] = updated_cost
                    heappush(hq, (updated_cost, nxt_node))
                    
        return dist
    
    dist_start = dijkstra(s)
    dist_a = dijkstra(a)
    dist_b = dijkstra(b)
    
    min_cost = dist_start[a] + dist_start[b]
    for i in range(1, n+1):
        if dist_start[i] + dist_a[i] + dist_b[i] < min_cost:
            min_cost = dist_start[i] + dist_a[i] + dist_b[i]
            
    return min_cost
    
# 플로이드 워샬 활용
import sys

def solution(n, s, a, b, fares):
    dist = [[sys.maxsize] * (n+1) for _ in range(n+1)]
    
    for i in range(n+1):
        dist[i][i] = 0
    
    for start, end, cost in fares:
        dist[start][end] = cost
        dist[end][start] = cost
        
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    answer = sys.maxsize
    for i in range(1, n+1):
        answer = min(answer, dist[s][i] + dist[i][a] + dist[i][b])
            
    return answer