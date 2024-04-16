# 상어의 냄새는 k번 이동하고 나서 사라진다.
# 상어의 이동
    # 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡음
    # 그런 칸이 없다면 자신의 냄새가 있는 칸의 방향으로 잡음
    # 가능한 칸이 여러개일 수 있는데 우선순위를 따름

# 매초에 냄새를 어떻게 업데이트할 것인가?
# 최대 초 * 냄새 위치 = O(1000 * 400)
# 행렬을 돌며 냄새의 초를 -1시키자

import sys
from collections import defaultdict
input = sys.stdin.readline

n, m, k = map(int, input().split())

# 격자 입력받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 상어의 냄새 초기화
# 냄새 유지 초가 == k라면 상어의 위치가 된다.
smell = [[[-1, -1] for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            smell[i][j] = [graph[i][j], k]

# 상어의 방향 입력받기
shark_dir = [-1] + list(map(int, input().split()))

# 각 상어의 우선순위 입력받기
priority = [[-1]]
for i in range(m):
    pri_lst = defaultdict(list)
    for i in range(1, 5):
        pri_lst[i] = list(map(int, input().split()))
    priority.append(pri_lst)

# 시간에 따른 상어의 이동
## 이동을 위한 dx, dy 저장
dir = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}

def move(shark_num, bx, by, nx, ny, d):
    # 더 작은 번호를 가진 상어가 생존
    if graph[nx][ny] != 0:
        if graph[nx][ny] < shark_num:
            graph[bx][by] = 0
            shark_dir[shark_num] = -1
        else:
            # 상어 위치 업데이트
            # 격자 벗어난 상어 체크
            # 새로운 상어 방향 업데이트
            graph[bx][by] = 0
            shark_dir[graph[nx][ny]] = -1
            shark_dir[shark_num] = d
            graph[nx][ny] = shark_num
    else:
            # 상어 위치 업데이트
            # 격자 벗어난 상어 체크
            # 새로운 상어 방향 업데이트
            graph[bx][by] = 0
            shark_dir[shark_num] = d
            graph[nx][ny] = shark_num
    
    update_smell(nx, ny, graph[nx][ny], k)

# 냄새 업데이트
def update_smell(nx, ny, shark_num, amount):
    if amount <= 0:
        smell[nx][ny] = [-1, -1]
    else:
        smell[nx][ny] = [shark_num, amount]

# 1을 제외한 상어의 존재 확인
def check_exist():
    for i in range(2, m+1):
        if shark_dir[i] != -1:
            return True
    else:
        return False

# 상어의 이동
time = 0
while check_exist() and time <= 1000:
    time += 1
    # 추후 한꺼번에 이동하기 위해 상어의 이동 저장
    tmp_move = []

    for i in range(n):
        for j in range(n):

            # 해당 위치에 상어가 존재하는지 확인
            if graph[i][j] != 0:
                shark, duration = smell[i][j]
                # 현재 상어의 방향
                cur_dir = shark_dir[shark]
                # 해당 상어의 방향의 우선순위 가져오기
                cur_pri = priority[shark][cur_dir]

                # 갈 수 있는 방향 우선순위순으로 확인
                no_smell_zone = []
                my_smell_zone = []
                for d in cur_pri:
                    dx, dy = dir[d]
                    nx = i + dx
                    ny = j + dy

                    # 갈 수 있는지 확인(단순히 격자 안인지)
                    if 0<=nx<n and 0<=ny<n:
                        n_shark, n_duration = smell[nx][ny]
                        # no smell zone일 경우
                        if n_shark == -1:
                            no_smell_zone.append([nx, ny, d])
                        # my smell zone일 경우
                        elif n_shark == shark:
                            my_smell_zone.append([nx, ny, d])

                # 만약 no smell zone이 있다면?
                if len(no_smell_zone) >= 1:
                    x, y, d = no_smell_zone[0]
                    tmp_move.append([shark, i, j, x, y, d])
                    
                # 만약 my smell zone이 있다면?
                elif len(my_smell_zone) >= 1:
                    x, y, d = my_smell_zone[0]
                    tmp_move.append([shark, i, j, x, y, d])

    # 향기 업데이트
    for i in range(n):
        for j in range(n):
            # 향기가 있다면
            if smell[i][j][0] != -1:
                shark, duration = smell[i][j]
                update_smell(i, j, shark, duration-1)

    # 상어 위치 업데이트
    for case in tmp_move:
        shark, nx, ny, dx, dy, d = case
        move(shark, nx, ny, dx, dy, d)

# 1을 제외한 다른 상어가 남아있지 않을 경우
if not check_exist():
    # 1000초를 넘었다면 -1, 아니라면 time 출력
    print(time if time <= 1000 else -1)
# 1000를 넘었는데도 다른 상어가 남아있는 경우
else:
    print(-1)