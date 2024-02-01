# 브루트 포스 - dfs, 백트레킹

# x, y를 기준으로 하지 않고, depth를 기준으로 한다.
# 오른쪽과 아래쪽만을 확인해도 모든 묶음을 확인할 수 있다.
import sys
input = sys.stdin.readline

# O(4*4*4*2)
def dfs(depth, sum):
    global answer
    if depth == d:
        answer = max(answer, sum)
        return
        
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue

            for k in range(2):
                nx = i+dx[k]
                ny = j+dy[k]

                if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
                    visited[i][j] = True
                    visited[nx][ny] = True
                    dfs(depth+1, sum + park[i][j] + park[nx][ny])
                    visited[i][j] = False
                    visited[nx][ny] = False
    
answer = 0
n = int(input()) # n 받아오기

park = [] # 나무 정보 받아오기
for _ in range(n):
    park.append(list(map(int, input().split())))

dx = [0,1]
dy = [1,0]

visited = [[False] * n for _ in range(n)]
d = 2 if n == 2 else 4
dfs(0, 0)
print(answer)