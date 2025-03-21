# 직사각형 테두리 직접 그리기
# 시간 복잡도: 최대 1000 * 8000
import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
dq = deque()

visited = [[False] * 2001 for _  in range(2001)]

def bfs(x, y):
    dq.append((x, y))
    visited[x][y] = True

    while dq:
        cx, cy = dq.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0<=nx<=2000 and 0<=ny<=2000:
                if rec[nx][ny] == 1 and not visited[nx][ny]: 
                    visited[nx][ny] = 1
                    dq.append((nx, ny))

n = int(input())
rec = [[0] * 2001 for _  in range(2001)]
start= []

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += 500; y1 += 500; x2 += 500; y2 += 500
    x1 *= 2; y1 *= 2; x2 *= 2; y2 *= 2
    start.append([x1, y1])

    # 직사각형 테두리 표시
    for i in range(x1, x2+1):
        if i == x1 or i == x2:
            for j in range(y1, y2+1):
                rec[i][j] = 1
        else:
            rec[i][y1] = 1
            rec[i][y2] = 1

ans = 0
for i in range(len(start)):
    x, y = start[i]
    if not visited[x][y]:
        bfs(x, y)
        ans += 1

if visited[1000][1000]:
    ans -= 1
print(ans)

# 누적합 풀이 
# 시간 복잡도: O(n**2)

"""
풀이 방법
1. 직사각형 위치 누적합 (n**2)
2. 누적합이된 것을 바탕으로 dfs / bfs (n**2)
    - 다니면서 (0,0) 포함하는지 확인
    - dfs / bfs가 진행되는 횟수 cnt
3. (0,0)을 포함하는지에 따라 달라짐
    - 포함: cnt - 1
    - 미포함: cnt

- 잘못 생각한 부분 - 사각형 안에 사각형은 한 선으로 갈 수 없다.
    - 해결: 누적합을 계산할 떄 사각형 가운데는 누적하지 않음

- 잘못 생각한 부분 - (1, 1)/(4, 4) and (2, 2)/(3, 3)
    위의 경우는 한 번에 그릴 수 없지만, 지금 방식으로는 bfs에 의해 한 번으로 처리가 됨
    - 해결: 좌표 * 2를 하면 깔끔하게 해결
"""

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
rec = []
prefix = [[0] * 2001 for _ in range(2001)]
group_cnt = 0

# 직사각형 누적합 정보 저장
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += 500; y1 += 500; x2 += 500; y2 += 500
    x1 *= 2; y1 *= 2; x2 *= 2; y2 *= 2
    prefix[x1][y1] += 1
    if x2 < 2000:
        prefix[x2+1][y1] -= 1
    if y2 < 2000:
        prefix[x1][y2+1] -= 1
    if x2 < 2000 and y2 < 2000:
        prefix[x2+1][y2+1] += 1

    # 직사각형 안 누적합 없애기
    prefix[x2][y2] -= 1
    if x1 < 2000 and y1 < 2000:
        prefix[x1+1][y1+1] -= 1
    if x1 < 2000:
        prefix[x1+1][y2] += 1
    if y1 < 2000:
        prefix[x2][y1+1] += 1

    if (1000 in (x1, x2) and y1 <= 1000 <= y2) or (1000 in (y1, y2) and x1 <= 1000 <= 2):
        group_cnt = -1

# 누적합 계산
for i in range(2001):
    for j in range(2001):
        if i > 0 and j > 0:
            prefix[i][j] -= prefix[i-1][j-1]
        if i > 0:
            prefix[i][j] += prefix[i-1][j]
        if j > 0:
            prefix[i][j] += prefix[i][j-1]

# bfs 진행
visited = [[False] * 2001 for _ in range(2001)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy):
    dq = deque()
    dq.append((sx, sy))
    visited[sx][sy] = True

    while dq:
        cx, cy = dq.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0<=nx<=2000 and 0<=ny<=2000 and prefix[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                dq.append((nx, ny))

for i in range(2001):
    for j in range(2001):
        if prefix[i][j] != 0 and not visited[i][j]:
            group_cnt += 1
            bfs(i, j)

print(group_cnt)

# union find 풀이

import sys
input = sys.stdin.readline

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa < pb:
        parent[pb] = parent[pa]
    else:
        parent[pa] = parent[pb]

def isCrossed(a, b):
    x1, y1, x2, y2 = points[a]
    x3, y3, x4, y4 = points[b]

    if x3 > x2 or x4 < x1 or y3 > y2 or y4 < y1:
        return False
    
    if x1 < x3 and x4 < x2 and y1 < y3 and y4 < y2:
        return False
    
    if x3 < x1 and x2 < x4 and y3 < y1 and y2 < y4:
        return False
    
    return True

n = int(input())
points = []
original = False
parent = [i for i in range(n)]
answer = 0

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    points.append([x1, y1, x2, y2])

    if x1 == 0 or x2 == 0:
        if y1 <= 0 <= y2:
            answer = -1
    
    if y1 == 0 or y2 == 0:
        if x1 <= 0 <= x2:
            answer = -1

for i in range(n-1):
    for j in range(i+1, n):
        if isCrossed(i, j):
            union(i, j)

for i in range(n):
    if parent[i] == i:
        answer += 1

print(answer)

# dict을 사용한 union find

"""
- 한붓 그리기
- 직사각형 그룹화
"""

import sys
input = sys.stdin.readline

rec_group = {}
start_contain = False

# 직사각형 순서에 따라 그룹핑이 달라짐
n = int(input())
for i in range(n):
    x, y, a, b = map(int, input().split())

    # 시작 거북이 포함하는지 확인
    if ((x == 0 or a == 0) and y<=0<=b) or ((y == 0 or b == 0) and x<=0<=a):
        start_contain = True

    # 초기 직사각형 넣기
    if len(rec_group.keys()) == 0:
        rec_group[i] = [(x, y, a, b)]
        continue

    # 그룹화 진행
    new_group = []
    for group_index in rec_group.keys():
        for gx, gy, ga, gb in rec_group[group_index]:
            # 외부에 존재
            if gx > a or ga < x or b < gy or y > gb:
                continue
            # 내부에 존재
            if (gx < x and (gx < x and a < ga and gy < y and b < gb)) or (gx > x and (x < gx and ga < a and y < gy and gb < b)):
                continue
            else:
                new_group.append(group_index)
                break
    
    grouping = [(x, y, a, b)]
    for group_index in new_group:
        grouping += rec_group.get(group_index, [])
        rec_group.pop(group_index, None)

    rec_group[i] = grouping

group_size = len(rec_group.keys())
print(group_size - 1 if start_contain else group_size)