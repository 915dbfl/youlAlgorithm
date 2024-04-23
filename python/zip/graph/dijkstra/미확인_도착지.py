# s에서 출발, 목적지 후보 중 하나로 이동할 것임
# 최단거리로 이동할 것임
# 그들이 지난 길 중 일부를 안다.
# 그들의 최종 목적지를 추론하자
    # 목적지 후보 오름차순 정렬해 출력

# 최단 경로가 여러개 나오는 경로

# 오답..
import sys
from collections import defaultdict
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

# 다익스트라 -> O(nm)
def getCandi(start, g, h):
    global n
    hq = []
    heappush(hq, (0, start))
    # start에서 각 노드까지의 최단 거리 저장
    dist = [INF] * (n+1)
    dist[start] = 0
    # gh를 지나가는 여부 체크
    checkGH = [False] * (n+1)

    while hq:
        d, cur = heappop(hq)

        if dist[cur] < d: continue

        for nd, nxt in graph[cur]:
            if dist[nxt] > d + nd:
                dist[nxt] = d + nd
                checkGH[nxt] = checkGH[cur]
                 # 현재 gh를 지나는 경우 업데이트
                if len(set([cur, nxt]) & set([g, h])) == 2:
                    checkGH[nxt] = True
                heappush(hq, (d+nd, nxt))
            # 최단 경로가 여러 개 나올 경우 대비
            elif dist[nxt] == d + nd:
                if checkGH[nxt] or checkGH[cur]:
                    checkGH[nxt] = True
                # 현재 gh를 지나는 경우 업데이트
                if len(set([cur, nxt]) & set([g, h])) == 2:
                    checkGH[nxt] = True
                heappush(hq, (d+nd, nxt))
 
    return dist, checkGH

t = int(input())
for _ in range(t):
    # 교차로, 도로, 목적지 후보의 개수
    n, m, t = map(int, input().split())

    # s: 출발지, 듀오가 지나간 거리 g-h
    s, g, h = map(int, input().split())

    # 양방향 도로 저장
    graph = defaultdict(list)
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((d, b))
        graph[b].append((d, a))

    candis = set()
    for _ in range(t):
        candis.add(int(input()))

    # 최단거리와 gh를 지나는 여부 리스트 받아오기
    dist, case = getCandi(s, g, h)

    answer = set()
    for i in range(n+1):
        # gh를 지나고 후보에 존재하고, 갈 수 있는 거리라면
        if case[i]:
            answer.add(str(i))
    result = list(candis & answer)
    result.sort()

    print(" ".join(result))