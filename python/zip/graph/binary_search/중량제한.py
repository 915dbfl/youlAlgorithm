import sys
from heapq import heappush, heappop
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
bridges = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    # 양방향 다리 저장
    bridges[a].append((-c, b))
    bridges[b].append((-c, a))

A, B = map(int, input().split())
hq = []
minWeight = -10**9 - 1
visited = [False] * (n+1)
visited[A] = True

# 최소 중량, 현재 위치
heappush(hq, (-10**9, A))
while hq:
    weight, cur = heappop(hq)
    # 다익스트라는 방문 표시를 큐에서 뺀 후 진행해야 함
    # 처음으로 값을 갱신할 때가 최적이라는 보장이 없기 때문
    visited[cur] = True 

    # B에 도착한 경우, 제일 처음 값이 최적의 해
    if cur == B: 
        minWeight = -weight
        break

    # 가지 치기
    if -weight <= minWeight:
        continue
    
    # 모든 다리 확인
    for nw, nn in bridges[cur]:
        # 최소 중량 구하기
        rw = min(-weight, -nw)
        # 더 큰 최소 중량이라면
        if rw > minWeight and not visited[nn]:
            heappush(hq, (-rw, nn))

print(minWeight)

# 이분 탐색 + dfs / bfs
import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def bfs(target):
    dq = deque()
    dq.append(A)
    visited = [False] * (n+1)
    visited[A] = True

    while dq:
        cur = dq.popleft()

        if cur == B:
            return True

        for nx, nw in bridges[cur]:
            if nw >= target and not visited[nx]:
                visited[nx] = True
                dq.append(nx)

    return False

n, m = map(int, input().split())
bridges = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    # 양방향 다리 저장
    bridges[a].append((b, c))
    bridges[b].append((a, c))

A, B = map(int, input().split())

start = 1
end = 10**9

result = 0
while start <= end:
    mid = (start + end) // 2

    if bfs(mid):
        result = mid
        start = mid + 1
    else:
        end = mid -1

print(result)