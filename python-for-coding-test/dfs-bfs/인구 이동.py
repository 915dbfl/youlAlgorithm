# 오답, 다시 풀어보기
import sys
from collections import deque

n, l, r = map(int, input().split())
populations = []
visited = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 국가 인구수 저장
for _ in range(n):
    populations.append(list(map(int, sys.stdin.readline().split())))

def bfs(x, y):
    dq = deque([[x, y]])
    visited[x][y] = 1
    united_cities = [[x, y]]
    pops = populations[x][y]

    while dq:
        cx, cy = dq.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0<= nx < n and 0<= ny < n and visited[nx][ny] == 0:
                if l <= abs(populations[cx][cy] - populations[nx][ny]) <= r: # 인구 차이가 l 이상, r 이하일 경우
                    # 연합에 추가 작업
                    visited[nx][ny] = 1 
                    united_cities.append([nx, ny])
                    pops += populations[nx][ny]
                    dq.append([nx, ny])

    new_pop = pops // len(united_cities)
    for a, b in united_cities:
        populations[a][b] = new_pop

    return len(united_cities) > 1 # 인구 이동했는지 반환

day = 0
while 1:
    open = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                open = open | bfs(i, j)

    if open:
        day += 1
    else:
        print(day)
        break