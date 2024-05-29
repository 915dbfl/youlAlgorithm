# 45분
import sys
input = sys.stdin.readline

m, n = map(int, input().split())

# 지도 입력받기
Map = []
for _ in range(m):
    Map.append(list(input()))

# wall dp 값을 저장할 배열 [상, 하, 좌, 우]
wall = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(m)]

# 지도 속 모든 위치 확인해 벽 누적값 구하기
for i in range(1, m):
    for j in range(1, n):
        if Map[i][j] == ".": # 빈 공간이라면
            # 상: 위에 빈 공간이 없을 경우
            if Map[i-1][j] != ".":
                wall[i][j][0] = wall[i][j-1][0] + 1
            # 좌: 왼쪽에 빈 공간이 없을 경우
            if Map[i][j-1] != ".":
                wall[i][j][2] = wall[i-1][j][2] + 1
        else: # 벽이라면
            # 상: 위에 빈 공간이라면(빈공간 기준으로는 하)
            if Map[i-1][j] == ".":
                wall[i-1][j][1] = wall[i-1][j-1][1] + 1
            # 좌: 위에 빈 공간일 경우(빈공간 기준으로는 우)
            if Map[i][j-1] == ".":
                wall[i][j-1][3] = wall[i-1][j-1][3] + 1

answer = 0
for i in range(1, m):
    for j in range(1, n):
        if wall[i][j][0] == 0: # 위쪽 벽이 0이 되었을 때
            answer += wall[i][j-1][0] // 2
        if wall[i][j][1] == 0: # 아랫쪽 벽이 0이 되었을 때
            answer += wall[i][j-1][1] // 2

for i in range(1, n):
    for j in range(1, m):
        if wall[j][i][2] == 0: # 왼쪽 벽이 0이 되었을 때
            answer += wall[j-1][i][2] // 2
        if wall[j][i][3] == 0: # 왼쪽 벽이 0이 되었을 때
            answer += wall[j-1][i][3] // 2

print(answer)

# 다른 풀이

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
gallery = [list(input()) for _ in range(n)]

answer = 0

def pic(obj1, obj2, n, m, x, y):
    global answer

    rc = [0, 0]

    for rc[x] in range(n-1):
        cnt = 0
        for rc[y] in range(m):
            print(rc)
            if gallery[rc[0]][rc[1]] == obj1 and gallery[rc[0] + y][rc[1] + x] == obj2:
                cnt += 1
            else:
                answer += cnt // 2
                cnt = 0

# 사진을 걸 수 있는 조건
# [벽, 복도], [복도, 벽]
for obj1, obj2 in [['X', '.'], ['.', 'X']]:
    # 행에 따라 탐색
    pic(obj1, obj2, n, m, 0, 1)
    # 열에 따라 탐색
    pic(obj1, obj2, m, n, 1, 0)

print(answer)