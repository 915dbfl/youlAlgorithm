import sys
from collections import defaultdict

n, k = map(int, sys.stdin.readline().split())
tube = []
virus = defaultdict(list)

dx = [-1, 1, 0 , 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    tube.append(list(map(int, sys.stdin.readline().split())))

s, tx, ty = map(int, input().split()) # s초 뒤 x, y 위치의 값은?

# 바이러스 위치 파악
def get_virus_index():
    for i in range(1, k+1):
        virus[i] = []

    for i in range(n):
        for j in range(n):
            if tube[i][j] != 0:
                virus[tube[i][j]].append([i, j]) # k인 바이러스 위치 저장

# 1초 동안 바이러스 전파
def virus_append(x, y, v):
    virus_list = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n and tube[nx][ny] == 0: # 아무 바이러스가 존재하지 않을 경우
            tube[nx][ny] = v
            virus_list.append([nx, ny])

    return virus_list

get_virus_index()
for _ in range(s): # 총 s초 동안 퍼뜨림
    for v in range(1, k+1): # 숫자가 작은 바이러스 부터 퍼뜨리기 시작
        add_virus = []
        for x, y in virus[v]:
            add_virus += virus_append(x, y, v)
        virus[v] = add_virus # 이전에 방문했던 위치는 다시 방문하지 않아도 된다.
        
print(tube[tx-1][ty-1])

# 예시 답안
# bfs 적절히 활용하기

from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    # 보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
            data.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기 (낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)
 
target_s, target_x, target_y = map(int, input().split())
 
# 바이러스가 퍼져나갈 수 있는 4가지의 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 너비 우선 탐색(BFS) 진행
while q:
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break
    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])