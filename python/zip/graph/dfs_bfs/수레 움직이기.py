"""
# 주요 정보
1. 각 턴마다 모든 수레를 인접한 칸으로 이동시킨다.
2. 이동 시 주의사항
    - 각 수레는 자신이 방문했던 곳을 재방문할 수 없다.
    - 목표하는 칸에 도착한다면 더 이상 움직이지 않는다.
    - 한 칸에는 오직 하나의 수레만
    - 수레끼리 자리 바꾸는 것도 불가

# 풀이 과정
1. 이차원 배열로 각 칸에 빨간 / 파란 수레 방문 여부 표시
2. dfs로 모든 경우의 수 확인
    - answer보다 move가 많다면 가지치기
3. 매턴마다 모든 수레를 움직인다? -> 그냥 각 수레가 움직이는 방식으로 해결하면 됨
"""
import sys

def solution(maze):
    
    def dfs(red, blue, isRed, rCnt, bCnt):
        nonlocal answer
        if maze[red[0]][red[1]] == 3 and maze[blue[0]][blue[1]] == 4:
            answer = min(answer, max(rCnt, bCnt))
            return
        
        if answer < max(rCnt, bCnt):
            return
        
        # 이미 목표에 도달한 경우 턴 넘기기
        if (isRed and maze[red[0]][red[1]] == 3) or (not isRed and maze[blue[0]][blue[1]] == 4):
            dfs(red, blue, not isRed, rCnt, bCnt)
            return
        
        # 턴에 따라 이동
        for i in range(4):
            cur = red if isRed else blue
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 방문하지 않았었고, 이동할 수 있다면
                if isRed:
                    if not visited[nx][ny][0] and maze[nx][ny] != 5 and blue != [nx, ny]:
                        visited[nx][ny][0] = True
                        dfs([nx, ny], blue, not isRed, rCnt + 1, bCnt)
                        visited[nx][ny][0] = False
                else:
                    # 방문하지 않았었고, 이동할 수 있다면
                    if not visited[nx][ny][1] and  maze[nx][ny] != 5 and red != [nx, ny]:
                        visited[nx][ny][1] = True
                        dfs(red, [nx, ny], not isRed, rCnt, bCnt+1)
                        visited[nx][ny][1] = False
        
    n = len(maze)
    m = len(maze[0])
    visited = [[[False, False] for _ in range(m)] for _ in range(n)]
    answer = sys.maxsize
    
    # 빨간 / 파란 수레 시작, 도착 칸 설정
    rs = [-1, -1]
    re = [-1, -1]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(n):
        for j in range(m):
            # 빨간 수레 시작 칸
            if maze[i][j] == 1:
                rs = [i, j]
                visited[i][j][0] = True
            # 파란 수레 시작 칸                
            elif maze[i][j] == 2:
                bs = [i, j]
                visited[i][j][1] = True
    
    # 빨간 수레 먼저 이동 or 파란 수레 먼저 이동 경우 모두 확인
    dfs(rs, bs, True, 0, 0)
    dfs(rs, bs, False, 0, 0)
    return answer if answer != sys.maxsize else 0