# 단순 브루트 포스
import sys
input = sys.stdin.readline

n = int(input())

relations = []
for i in range(n):
    relations.append(list(input().rstrip()))

friends = [set() for _ in range(n)]
result = [set() for _ in range(n)]

for i in range(n):
    for j in range(n):
        if relations[j][i] == "Y":
            friends[i].add(j)
            result[i].add(j)

for i in range(n):
    for j in range(n):
        if relations[j][i] == "Y":
            # 자기 자신 제거
            tmp = friends[i] - set([j])
            # 친구 추가
            result[j] |= tmp

ans = 0
for i in range(n):
    ans = max(ans, len(result[i]))
print(ans)

# 플로이드 워샬 알고리즘

import sys
input = sys.stdin.readline

n = int(input())
friends = [list(input()) for _ in range(n)]

connected = [[0]* n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if friends[i][j] == "Y" or (friends[i][k] == "Y" and friends[k][j] == "Y"):
                connected[i][j] = 1

ans = 0
for row in connected:
    ans = max(ans, sum(row))

print(ans)