#23.02.16
#알파벳
#알고리즘 스터디 : 백트래킹
#골드4

##dfs와 bfs의 차이
#bfs는 동시에 여러 경로를 진행하기 때문에 모든 경로를 큐에 다 들고 있어야 한다. -> 큐가 너무 커진다.
#dfs는 한 번에 하나의 경로만을 조사하기 때문에 아래와 같이 하나의 경로만 가지고 있어도 조사가 가능하다.
# --> 따라서 dfs는 조사해야 하는 경로 개수가 많아도 길이만 길지 않는다면 메모리 제한에 걸리지 않는다.

#시간초과: bfs
import sys
from collections import deque

def bfs():
    global answer
    q = deque()
    q.append((0, 0, set([lst[0][0]])))

    while q:
        x, y, s = q.popleft()

        if len(s) > answer:
            answer = len(s)

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<r and 0<=ny<c and lst[nx][ny] not in s:
                q.append((nx, ny, s | set([lst[nx][ny]])))


r, c = map(int, sys.stdin.readline().split())
lst = []
for _ in range(r):
    lst.append(list(sys.stdin.readline().rstrip()))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
answer = 1

bfs()

print(answer)

#시간초과: dfs
import sys

def dfs(x, y, s):
    global answer
    if len(s) > answer:
        answer = len(s)

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<r and 0<=ny<c and lst[nx][ny] not in s:
            dfs(nx, ny, s | set([lst[nx][ny]]))


r, c = map(int, sys.stdin.readline().split())
lst = []
for _ in range(r):
    lst.append(list(sys.stdin.readline().rstrip()))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
answer = 1

s = set()
s.add(lst[0][0])

dfs(0, 0, s)

print(answer)

#시간초과 해결
#메모리 초과 해결: 알파벳을 나타내는 배열을 선언해 global로 사용
import sys

def dfs(x, y, cnt):
    global answer
    if cnt > answer:
        answer = cnt

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<r and 0<=ny<c and alphabet[ord(lst[nx][ny])-65] == 0:
            alphabet[ord(lst[nx][ny])-65] = 1
            dfs(nx, ny, cnt+1)
            alphabet[ord(lst[nx][ny])-65] = 0


r, c = map(int, sys.stdin.readline().split())
lst = []
for _ in range(r):
    lst.append(list(sys.stdin.readline().rstrip()))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
answer = 1

alphabet =[0] * 26
alphabet[ord(lst[0][0]) - 65] = 1

dfs(0, 0, 1)

print(answer)