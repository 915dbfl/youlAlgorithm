# 끝나지 않는 파티

# 플로이드 워샬
import sys

n, m = map(int, sys.stdin.readline().split())
roads = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if roads[i][j] > roads[i][k] + roads[k][j]:
                roads[i][j] = roads[i][k] + roads[k][j]

for _ in range(m):
    cur, nxt, left = map(int, sys.stdin.readline().split())
    if roads[cur-1][nxt-1] <= left:
        print("Enjoy other party")
    else:
        print("Stay here")