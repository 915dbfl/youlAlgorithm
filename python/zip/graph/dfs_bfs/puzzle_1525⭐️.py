#23.03.03
#퍼즐
#골드2

#최소 이동: bfs
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
    q = deque()
    q.append(start)

    while q:
        n = q.popleft()

        if n == "123456789":
            return cntDict[n]

        pos = n.find("9")
        x = pos//3
        y = pos%3
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<3 and 0<=ny<3:
                nPos = nx*3+ny
                next = list(n)
                next[pos], next[nPos] = next[nPos], next[pos]
                next = "".join(next)

                if not cntDict.get(next):
                    q.append(next)
                    cntDict[next] = cntDict[n] + 1


start = ""
for _ in range(3):
    tmp = input().strip().replace(" ", "")
    start += tmp
start = start.replace("0", "9")

cntDict = dict()
cntDict[start] = 0

result = bfs()
print(result if result != None else -1)