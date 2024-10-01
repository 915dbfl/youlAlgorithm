import sys
input = sys.stdin.readline

n = int(input())
circles = []

for _ in range(n):
    num, x, r = map(int, input().split())
    # 원의 왼쪽, 원의 오른쪽 좌표 저장
    circles.append((x-r, x+r, num))

a, b = map(int, input().split())

# 왼쪽 좌표를 기준으로 오름차순 정렬
circles.sort()

# 각원의 부모 원을 찾아줄 스택
parent = [i for i in range(n+1)]
stack = [(1e9, 0)]

for i in range(n):
    left, right, idx = circles[i]

    # 왼쪽에 존재하는 원의 오른쪽이 현재 원의 왼쪽보다 작을 경우, 서로 겹치지 않음
    while stack[-1][0] < left:
        stack.pop()
        
    parent[idx] = stack[-1][1]
    stack.append((right, idx))

route_a = [a]
route_b = [b]

# 각자 route 추가
while a:
    a = parent[a]
    route_a.append(a)

while b:
    b = parent[b]
    route_b.append(b)

# 최초 공통 조상 저장
last = 0
while route_a and route_b and route_a[-1] == route_b[-1]:
    last = route_a[-1]
    route_a.pop()
    route_b.pop()

print(len(route_a) + len(route_b) + 1)
print(*route_a, last, *route_b[::-1])