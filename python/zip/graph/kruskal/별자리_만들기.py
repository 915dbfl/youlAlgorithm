# 최소 스패닝 트리(20분)
# 정렬하는 작업 > union-find
# O(ElogE)

import sys
input = sys.stdin.readline

# 별의 개수 입력 받음
n = int(input())
stars = []

# 별들의 x,y 좌표 입력 받기
for _ in range(n):
    x, y = map(float, input().split())
    stars.append((x, y))

# 별들의 서로 연결 dist 구하기
# O(n**2) -> O(10000)
link = []
for i in range(n):
    for j in range(i, n):
        # 자기 자신과의 거리 제외
        if i != j:
            x1, y1 = stars[i]
            x2, y2 = stars[j]

            dist = round((abs(x2 - x1)**2 + abs(y2 - y1)**2)**(0.5), 2)
            # 별들의 좌표 대신 인덱스로 기록
            link.append((dist, i, j))

# link dist 오름차순으로 정렬
link.sort(key = lambda x: x[0])

# union-find 실행
# 1. parent 초기화
parent = [i for i in range(n)]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find_parent(a):
    if parent[a] == a: return a
    else: return find_parent(parent[a])

# 2. 간선을 돌면 Union-find 진행
answer = 0
for dist, s1, s2 in link:
    if find_parent(s1) != find_parent(s2):
        answer += dist
        union(s1, s2)

print(answer)