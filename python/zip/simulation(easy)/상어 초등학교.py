# 1시간 13분
# 구현
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
idx = dict()

seat = [[0] * n for _ in range(n)]
degree = [[0] * n for _ in range(n)]
prefer = defaultdict(set)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 주변에 빈칸 개수 degree 배열에 저장
for i in range(n):
    for j in range(n):
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0<=nx<n and 0<=ny<n:
                degree[nx][ny] += 1

for _ in range(n**2):
    case = list(map(int, input().split()))
    tmp = [[0]*n for _ in range(n)]
    candi = [-1, -1, -1] # 좋아하는 학생 인접 개수, 위치
    
    # 들어갈 위치 구하기
    for pf in case[1:]:
        prefer[case[0]].add(pf)
        if pf in idx:
            px, py = idx[pf]
            #상하좌우 확인
            for i in range(4):
                nx = px + dx[i]
                ny = py + dy[i]

                # 범위 내고 아무도 존재하지 않는 위치일 경우
                if 0<=nx<n and 0<=ny<n and seat[nx][ny] == 0:
                    tmp[nx][ny] += 1
                    # 좋아하는 학생 인접 개수가 더 많을 경우
                    if tmp[nx][ny] > candi[0]:
                        candi = [tmp[nx][ny], nx, ny]
                    # 좋아하는 학생 인접 개수가 동일할 경우
                    elif tmp[nx][ny] == candi[0]:
                        # 비어있는 칸의 개수가 더 많을 경우
                        if degree[candi[1]][candi[2]] < degree[nx][ny]:
                            candi = [tmp[nx][ny], nx, ny]
                        # 비어있는 칸의 개수가 동일한 경우
                        elif degree[candi[1]][candi[2]] == degree[nx][ny]:
                            # 행열값 비교
                            if candi[1] > nx or (candi[1] == nx and candi[2] > ny):
                                candi = [tmp[nx][ny], nx, ny]
                            

    # 좋아하는 학생이 아직 아무도 위치가 정해지지 않았을 경우 들어갈 위치 구하기
    if candi[0] == -1:
        tmp_max = -1
        for i in range(n):
            for j in range(n):
                if seat[i][j] == 0 and degree[i][j] > tmp_max:
                    tmp_max = degree[i][j]
                    candi[1], candi[2] = i, j

    # 자리 배치
    seat[candi[1]][candi[2]] = case[0]
    idx[case[0]] = (candi[1], candi[2])
    # 주위 degree 감소
    for i in range(4):
        nx = candi[1] + dx[i]
        ny = candi[2] + dy[i]

        if 0<=nx<n and 0<=ny<n:
            degree[nx][ny] -= 1

# 전체 선호도 구하기
answer = 0
point = [0, 1, 10, 100, 1000]
for i in range(n):
    for j in range(n):
        nearf = set()
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0<=nx<n and 0 <=ny<n:
                nearf.add(seat[nx][ny])

        answer += point[len(prefer[seat[i][j]] & nearf)]

print(answer)

# 더 깔끔한 구현 but 시간은 조금 더 걸림
n = int(input())
data = [[0] * n for _ in range(n)]
students = [list(map(int, input().split())) for _ in range(n**2)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for student in students:
    available = []

    # 전체를 돌면서 가능한 자리인지 확인하기
    for i in range(n):
        for j in range(n):
            # 빈자리라면
            if data[i][j] == 0:
                prefer, empty = 0, 0

                # 상하좌우 방향 확인
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    # 범위내에 있을 때
                    if 0 <= nx < n and 0 <= ny < n:
                        # 좋아하는 학생이 주위에 있는지 확인
                        if data[nx][ny] in student[1:]:
                            prefer += 1
                        
                        # 빈자리가 있는지 확인
                        if data[nx][ny] == 0:
                            empty += 1

                available.append((i, j, prefer, empty))

    # 정렬
    available.sort(key = lambda x: (-x[2], -x[3], x[0], x[1]))
    data[available[0][0]][available[0][1]] = student[0]

answer = 0
score = [0, 1, 10, 100, 1000]
students.sort()

for i in range(n):
    for j in range(n):
        count = 0

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0<=nx<n and 0<=ny<n:
                if data[nx][ny] in students[data[i][j]-1]:
                    count += 1

        answer += score[count]

print(answer)