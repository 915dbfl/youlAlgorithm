#22.06.11
#게임 맵 최단거리

# 내 풀이(오답)
import sys
sys.setrecursionlimit(10**6)

def bfs(maps, cur, cnt):
    print(cur, cnt)
    if cur == goal:
        answer.append(cnt)
        return
    else:
        a, b = cur
        if b < goal[1] and maps[a][b+1] == 1:
            maps[a][b+1] = -1
            bfs(maps, (a, b+1), cnt+1)
        if a > 0 and maps[a-1][b] == 1:
            maps[a-1][b] = -1
            bfs(maps, (a-1, b), cnt+1)
        if b > 0 and maps[a][b-1] == 1:
            maps[a][b-1] = -1
            bfs(maps, (a, b-1), cnt+1)
        if a < goal[0] and maps[a+1][b] == 1:
            maps[a+1][b] = -1
            bfs(maps, (a+1, b), cnt+1)

def solution(maps):
    global goal, answer
    goal = (len(maps)-1, len(maps[0])-1)
    answer = []
    if maps[-1][-2] == 0 and maps[-2][-1] == 0:
        return -1
    else:
        bfs(maps, (0, 0), 1)
        return answer