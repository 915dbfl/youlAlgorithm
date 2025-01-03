answer = "z"
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
dAlpha = ["d", "l", "r", "u"]

def isValid(nx, ny, n, m):
    return 1<= nx <= n and 1 <= ny <= m

def dfs(n, m, x, y, r, c, prev_s, cnt, k):
    global answer
    
    # 최단거리를 가더라도 k를 넘는 경우 제외
    if k < cnt + abs(x-r) + abs(y-c):
        return
    
    if x == r and y == c and cnt == k:
        answer = prev_s
        return
    
    for i in range(4):
        # 미로 내에 존재하고 최소 문자열보다 사전순으로 앞에 있을 경우
        if isValid(x+dx[i], y+dy[i], n, m) and prev_s < answer:
            dfs(n, m, x+dx[i], y+dy[i], r, c, prev_s + dAlpha[i], cnt+1, k)

def solution(n, m, x, y, r, c, k):
    global answer
    dis = abs(x -r) + abs(y-c)
    if dis > k or (k-dis) % 2 == 1:
        return "impossible"
    
    dfs(n, m, x, y, r, c, "", 0, k)
    
    return answer
    
# queue를 활용한 dfs
from collections import deque
    
def solution(n, m, x, y, r, c, k):
    least_move = abs(x - r) + abs(y - c)

    if k < least_move or (k % 2) != (least_move % 2): 
        return "impossible"
    else:
        dq = deque()
        dq.append((x, y, ''))
        
        # 사전순에 따라 하좌우상 순서
        dx = [1, 0, 0, -1]
        dy = [0, -1, 1, 0]
        dir_str = ['d', 'l', 'r', 'u']
        
        while dq:
            curx, cury, route = dq.popleft()
            
            # dfs 정답 출력
            if curx == r and cury == c and len(route) == k:
                return route
            
            # 불필요한 경우 제거
            if len(route) == k:
                continue
                
            for i in range(4):
                nx = curx + dx[i]
                ny = cury + dy[i]
                
                if 1 <= nx <= n and 1 <= ny <= m:
                    # 해당 코드가 있어야 가장 최선을 선택할 수 있게 됨
                    if abs(r - nx) + abs(c - ny) + len(route) +1 > k: continue
        
                    dq.append((nx, ny, route + dir_str[i]))
                    break # 가장 최선의 경우만 선택
                    
        return "impossible"