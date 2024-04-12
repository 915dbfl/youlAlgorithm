from collections import defaultdict
from heapq import heappush, heappop
import sys
INF = sys.maxsize

def dijkstra(start, n):
    global dic
    hq = []
    dist = [INF] * (n+1)
    dist[start] = 0
    
    heappush(hq, (0, start))
    
    while hq:
        dis, cur = heappop(hq)
        
        if dist[cur] < dis: continue
        
        for nxt in dic[cur]:
            if dist[nxt] > dis + 1:
                dist[nxt] = dis + 1
                heappush(hq, (dis+1, nxt))
                
    return dist
    
# destination에서 dijkstra
def solution(n, roads, sources, destination):
    global dic
    dic = defaultdict(list)
    
    # 길 정보 저장
    for a, b in roads:
        dic[a].append(b)
        dic[b].append(a)
        
    dist = dijkstra(destination, n)
    answer = []
    for i in sources:
        if dist[i] == INF:
            answer.append(-1)
        else:
            answer.append(dist[i])
            
    return answer