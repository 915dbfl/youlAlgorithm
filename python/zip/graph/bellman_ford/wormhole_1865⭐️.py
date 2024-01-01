# #23.02.18
# #웜홀
# #골드3

#시간초과
import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline
INF = sys.maxsize

def road_dijkstra(start):
    h = [(0, start)]
    times = [INF] * (n+1)
    times[start] = 0

    while h:
        time, cur = heappop(h)

        if times[cur] < time:
            continue

        for tmp_time, tmp_next in roads[cur]:
            if times[tmp_next] > tmp_time+time:
                times[tmp_next] = tmp_time+time
                heappush(h, (tmp_time+time, tmp_next))
    return times

def worm_dijkstra(start):
    h = [(0, start)]
    times = [0] * (n+1)

    while h:
        time, cur = heappop(h)

        if times[cur] > time:
            continue
        
        if cur in holes.keys():
            for tmp_time, tmp_next in holes[cur]:
                if times[tmp_next] < tmp_time+time:
                    times[tmp_next] = tmp_time+time
                    heappush(h, (tmp_time+time, tmp_next))
    return times


case = int(input())

for _ in range(case):
    n, m, w = map(int, input().split())
    roads = defaultdict(list)
    holes = defaultdict(list)
    check = False

    for _ in range(m):
        s, e, t = map(int, input().split())
        roads[s].append((t, e))
        roads[e].append((t, s))

    for _ in range(w):
        s, e, t = map(int, input().split())
        holes[s].append((t, e))

    for h in holes.keys():
        go_dist = road_dijkstra(h) # h까지 걸리는 최단 시간
        back_dist = worm_dijkstra(h) # h에서 걸리는 최장 시간

        for i in range(1, n+1):
            if go_dist[i]-back_dist[i] < 0:
                print("YES")
                check = True
                break
        if check:
            break
    if not check:
        print("NO")

#리팩토링: 오답
#간선의 비용이 음의 경우, 다익스트라 알고리즘은 사용할 수 없다.
import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    h = [(0, start)]
    times = [INF] * (n+1)
    times[start] = 0

    while h:
        time, cur = heappop(h)

        if time < 0:
            return 1

        if times[cur] < time:
            continue
        
        for tmp_time, tmp_next in roads[cur]:
            if times[tmp_next] > tmp_time+time:
                times[tmp_next] = tmp_time+time
                heappush(h, (tmp_time+time, tmp_next))
    return 0

case = int(input())

for _ in range(case):
    n, m, w = map(int, input().split())
    roads = defaultdict(list)
    holes = []

    for _ in range(m):
        s, e, t = map(int, input().split())
        roads[s].append((t, e))
        roads[e].append((t, s))

    for _ in range(w):
        s, e, t = map(int, input().split())
        roads[s].append((-t, e))
        holes.append(e)

    for h in holes:
        if dijkstra(h):
            print("YES")
        else:
            print("NO")

# bellman ford: 시간초과
import sys
input = sys.stdin.readline
INF = int(1e9)

tc = int(input())

def bellmanFord(start):
    dist = [INF] * (n+1)
    dist[start] = 0

    for i in range(n):
        for s, e, t in edges:
            
            if dist[s] != INF and dist[e] > dist[s] + t:
                dist[e] = dist[s]+t

                if i == n-1:
                    return True

    return False

for _ in range(tc):
    n, m, w = map(int, input().split())
    edges = []

    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))


    check = 0
    for i in range(1, n+1):
        if bellmanFord(i):
            check = 1
            break
    if check:
        print("YES")
    else:
        print("NO")

# bellman ford: 리팩토링 (정답)
import sys
input = sys.stdin.readline
INF = int(1e9)

tc = int(input())

def bellmanFord():
    dist = [INF] * (n+1)

    for i in range(n):
        for s, e, t in edges:
            
            if dist[e] > dist[s] + t:
                dist[e] = dist[s]+t

                if i == n-1:
                    return True

    return False

for _ in range(tc):
    n, m, w = map(int, input().split())
    edges = []

    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))


    if bellmanFord():
        print("YES")
    else:
        print("NO")