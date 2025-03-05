"""
풀이 과정
1. 각 원의 부모를 구해야 함
    - y값은 0으로 고정되어 있음
    - 원의 양끝 x값을 바탕으로 부모-자식 관계 파악 가능 (트리 형태가 됨)
2. a와 b의 공통 조상까지의 부모 순서가 이동 경로를 나타냄 (트리이기 때문에 해당 경로는 한 개만이 존재함)
"""

import sys
input = sys.stdin.readline

class Circle:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def parent_lst(target):
    cur = target
    plst = [str(cur)]
    while parent[cur] != 0:
        plst.append(str(parent[cur]))
        cur = parent[cur]
    plst.append("0")

    return plst

def first_common_parent(plst1, plst2):
    idx = -1
    while plst1[idx] == plst2[idx]:
        idx -= 1

    return str(plst1[idx + 1])

n = int(input())
circles = [Circle(0, -sys.maxsize, sys.maxsize)]
for _ in range(n):
    k, x, r = map(int, input().split())
    circles.append(Circle(k, x - r, x + r))

circles.sort(key = lambda x: x.left)
parent = [0] * (n+1)
stack = [circles[0]]

for i in range(1, n):
    circle = circles[i]
    while stack and stack[-1].right < circle.left:
        stack.pop()

    if stack:
        parent[circle.value] = stack[-1].value
    stack.append(circle)

c1, c2 = map(int, input().split())
c1Parents = parent_lst(c1)
c2Parents = parent_lst(c2)

cp = first_common_parent(c1Parents, c2Parents)
cp_index1 = c1Parents.index(cp)
cp_index2 = c2Parents.index(cp)

root = c1Parents[:cp_index1+1] + c2Parents[:cp_index2][::-1]
print(len(root))
print(" ".join(root))