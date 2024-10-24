# 30분
import sys
sys.setrecursionlimit(500*500 + 1)
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]

def dfs(x, y):

    global answer
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            nDirKey = board[nx][ny]

            if nx + dir[nDirKey][0] == x and ny + dir[nDirKey][1] == y:
                if canExit[nx][ny]: continue
                answer += 1
                canExit[nx][ny] = True
                dfs(nx, ny)


canExit = [[False] * m for _ in range(n)]
dir = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

# 상하
for i in range(m):
    if board[0][i] == "U" and not canExit[0][i]:
        canExit[0][i] = True
        answer += 1
        dfs(0, i)
    if board[n-1][i] == "D" and not canExit[n-1][i]:
        canExit[n-1][i] = True
        answer += 1
        dfs(n-1, i)
# 좌우
for i in range(n):
    if board[i][0] == "L" and not canExit[i][0]:
        canExit[i][0] = True
        answer += 1
        dfs(i, 0)
    if board[i][m-1] == "R" and not canExit[i][m-1]:
        canExit[i][m-1] = True
        answer += 1
        dfs(i, m-1)

print(answer)

# 개선된 풀이
# 확실히 재귀보다 queue를 사용한 dfs가 빠름: 564ms -> 220ms

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]

def dfs(x, y):
    global answer
    dq = deque()
    dq.append((x, y))

    while dq:
        cx, cy = dq.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                nDirKey = board[nx][ny]

                if nx + dir[nDirKey][0] == cx and ny + dir[nDirKey][1] == cy:
                    if canExit[nx][ny]: continue
                    answer += 1
                    canExit[nx][ny] = True
                    dq.append((nx, ny))

canExit = [[False] * m for _ in range(n)]
dir = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

# 상하
for i in range(m):
    if board[0][i] == "U" and not canExit[0][i]:
        canExit[0][i] = True
        answer += 1
        dfs(0, i)
    if board[n-1][i] == "D" and not canExit[n-1][i]:
        canExit[n-1][i] = True
        answer += 1
        dfs(n-1, i)
# 좌우
for i in range(n):
    if board[i][0] == "L" and not canExit[i][0]:
        canExit[i][0] = True
        answer += 1
        dfs(i, 0)
    if board[i][m-1] == "R" and not canExit[i][m-1]:
        canExit[i][m-1] = True
        answer += 1
        dfs(i, m-1)

print(answer)

# 또 다른 dfs 풀이

import sys
from collections import deque

input = sys.stdin.readline

def dfs(ci, cj):
    q = deque()
    visited[ci][cj] = (ci, cj)
    q.append((ci, cj))
    # 경로에 있는 블록이 모두 탈출 가능한 블록
    cnt = 0

    while q:
        curx, cury = q.popleft()
        cnt += 1

        di, dj = direction_dict[arr[curx][cury]]
        ni, nj = curx + di, cury + dj
        
        if ni < 0 or ni >= N or nj < 0 or nj >= M: # 미로 탈출 조건
            answer_arr[ci][cj] = 1 # 정답 경로에 넣고 탈출
            return cnt
        
        if answer_arr[visited[ni][nj][0]][visited[ni][nj][1]] == 1:  # 해당 영역이 정답 set에 있으면 정답 처리
            answer_arr[ci][cj] = 1
            return cnt
        
        if visited[ni][nj] == (-1, -1):
            visited[ni][nj] = (ci, cj)
            q.append((ni, nj))

    return 0
    
N, M = map(int, input().strip().split())
arr = [list(input().strip()) for _ in range(N)]
direction_dict = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}

ans = 0
visited = [[(-1, -1)] * M for _ in range(N)]
# 방문한다고 다 탈출하는 것이 아니기 때문에
# 방문한 영역을 visited에 저장, 방문 후 탈출한 곳을 answer_arr에 저장
answer_arr = [[0] * M for _ in range(N)]
area_num = 1

for i in range(N):
    for j in range(M):
        if visited[i][j] == (-1, -1):
            ans += dfs(i, j)

print(ans)

# dp 풀이
import sys
sys.setrecursionlimit(300000)

def go(i, j):
    # Base case : 밖으로 나가는 경우
    if i < 0 or i > n - 1 or j < 0 or j > m - 1:
        return 1
    # Memoization
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = 0
    # 점화식
    dp[i][j] = max(dp[i][j], go(i + cache[arr[i][j]][0], j + cache[arr[i][j]][1]))
    return dp[i][j]

n, m = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]
cache = {'L' : (0, -1), 'R' : (0, 1), 'U' : (-1, 0), 'D' : (1, 0)}
ans = 0

for i in range(n):
    for j in range(m):
        # 아직 방문하지 않은 경우
        if dp[i][j] == -1:
            # 밖으로 갈 수 있다면 정답 증가
            if go(i, j) != 0:
                ans += 1
        # 방문했고 밖으로 나갈 수 있는 경우 정답 증가
        elif dp[i][j] == 1:
            ans += 1
        
print(ans)