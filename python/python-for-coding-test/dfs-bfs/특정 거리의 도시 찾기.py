# 모든 간선의 비용이 1
# 따라서 bfs를 통해 쉽게 최단 거리를 찾을 수 있다.

import sys
from collections import defaultdict, deque

n, m, k, x= map(int, sys.stdin.readline().split())
road = defaultdict(list)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    road[a].append(b)

# 거리가 target인 도시들 구하기
def bfs(n, start, target):
    dq = deque([[start, 0]]) # 시작 위치 추가
    visited = [0]*(n+1) # 방문 여부를 저장할 배열
    visited[start] = 1  # 시작 위치는 방문으로 체크

    while dq:
        cur, dis = dq.popleft() # bfs이므로 popleft

        if dis > target: # bfs이므로 target을 넘어가는 거리의 경우 break
            break
        elif dis == target:  # target 거리라면
            answer.append(cur)
        elif dis < target: # target 거리보다 가깝다면 다음 도시들 탐색
            for nxt in road[cur]:
                if visited[nxt] == 0: # nxt 방문이 최단거리라면
                    visited[nxt] = 1 # nxt 방문으로 체크
                    dq.append([nxt, dis+1])
            

answer = []
bfs(n, x, k)
answer.sort()

if len(answer) == 0:
    print(-1)
else:
    for c in answer:
        print(c)

# 예시 답안
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+ 1)]

# 모든 도로 정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n+1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# bfs 수행
# 최단 거리 O(노드 수 n + 간선 수 m)
q = deque([x])
while q:
    now = q. popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)