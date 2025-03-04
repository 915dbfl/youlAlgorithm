"""
풀이 과정
1. 각 원의 부모를 구해야 함
    - y값은 0으로 고정되어 있음
    - 원의 양끝 x값을 바탕으로 부모-자식 관계 파악 가능 (트리 형태가 됨)
2. a와 b의 공통 조상까지의 부모 순서가 이동 경로를 나타냄 (트리이기 때문에 해당 경로는 한 개만이 존재함)
"""

import sys
input = sys.stdin.readline
from collections import deque

class Circle:
    def __init__(self, k, left, right):
        self.k = k
        self.left = left
        self.right = right

n = int(input())
circles = [Circle(0, -sys.maxsize, sys.maxsize)]

for _ in range(n):
    k, x, r = map(int, input().split())
    circles.append(Circle(k, x-r, x+r))

circles.sort(key = lambda circle: circle.left)
parents = [0] * (n+1)
stack = [circles[0]]

for i in range(1, n+1):
    cur = circles[i]
    while stack[-1].right < cur.left:
        stack.pop()
    
    parents[i] = stack[-1].k
    stack.append(cur)

a, b = map(int, input().split())
a_parents = [a]
b_parents = [b]
cur = a

while True:
    a_parents.append(parents[cur])
    if parents[cur] == 0:
        break
    cur = parents[cur]

cur = b
common_p = -1
while parents[cur] != 0:
    if parents[cur] in a_parents:
        common_p = parents[cur]
        break
    b_parents.append(parents[cur])
    cur = parents[cur]

for parent in a_parents:
    print(parent, end = " ")
    if (parent == common_p):
        break

for parent in b_parents[::-1]:
    print(parent, end = " ")