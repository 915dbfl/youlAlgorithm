#23.02.07
#파티
#골드3
#모든 정점에서 다른 모든 정점까지의 거리를 구하는 문제
#플로이드 워셜은 n의 크기가 작을 때
#그 외는 다익스트라를 이용하도록 하자!

#플로이드 워셜 - 시간초과
import sys
n, m, x = map(int, sys.stdin.readline().split())
graph = [[100]*n for _ in range(n)]

for _ in range(m):
    s, e, t = map(int, sys.stdin.readline().split())
    graph[s-1][e-1] = t

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0

            elif graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

time = [0]*n
for i in range(n):
    time[i] = graph[i][x-1] + graph[x-1][i]

print(max(time))

#다익스트라
import sys
from collections import defaultdict
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    h = [(0, start)]
    times = [INF] * (n+1)
    times[start] = 0

    while h:
        time, cur = heappop(h)

        if times[cur] < time:
            continue
    
        for nt, nc in dic[cur]:
            if times[nc] > time+nt:
                times[nc] = time+nt
                heappush(h, (time+nt, nc))

    return times

n, m, x = map(int, input().split())
dic = defaultdict(list)

for _ in range(m):
    s, e, t = map(int, input().split())
    dic[s].append((t, e))

graph = [[0]*(n+1)]
for i in range(1, n+1):
    graph.append(dijkstra(i))

answer = 0
for i in range(1, n+1):
    answer = max(answer, graph[i][x]+graph[x][i])

print(answer)

#다익스트라 새로운 접근 방법
#가야하는 곳이 x
#단순 다익스트라로는 모든 정점 -> 모든 정점을 계산!
#살짝 다르게 생각한다면 x -> 모든 정점과
#단방향 도로를 거꾸로 생각해서 x -> 모든 정점을 구한다면
#모든 정점 -> x, x -> 모든 정점을 구할 수 있게 된다!
import sys
from collections import defaultdict
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start, dic):
    h = [(0, start)]
    times = [INF] * (n+1)
    times[start] = 0

    while h:
        time, cur = heappop(h)

        if times[cur] < time:
            continue
    
        for nt, nc in dic[cur]:
            if times[nc] > time+nt:
                times[nc] = time+nt
                heappush(h, (time+nt, nc))

    return times

n, m, x = map(int, input().split())
go_dic = defaultdict(list)
back_dic = defaultdict(list)

for _ in range(m):
    s, e, t = map(int, input().split())
    go_dic[s].append((t, e))
    back_dic[e].append((t, s))

go = dijkstra(x, go_dic)
back = dijkstra(x, back_dic)

dis = [i+j for i, j in zip(go, back)]
print(max(dis[1:]))