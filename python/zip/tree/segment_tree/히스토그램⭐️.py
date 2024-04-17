# stack 이용하기
import sys
input = sys.stdin.readline

n = int(input())

height = []
for _ in range(n):
    height.append(int(input()))

stack = []
answer = 0
for i in range(n):
    h = height[i]
    while stack and stack[-1][1] > h:
        bi, bh = stack.pop()
        tmpSize = (i-bi) * bh
        answer = max(answer, tmpSize)
    
    stack.append((i, h))
    print(stack, answer)

while stack:
    ci, ch = stack.pop()
    tmpSize = (n-ci) * ch
    answer = max(answer, tmpSize)

print(answer)

# 세그먼트 트리
    # 구간별로 가장 작은 높이 값을 가지는 직사각형 idx wjwkd
    # 전체 구간에서부터 가장 작은 직사각형의 높이값 * 그 구간의 길이 = 가장 큰 직사각형 넓이값
    # 분할정복을 사용해 좌, 우로 구간을 나눠 넓이값 비교
    # 전체, 좌, 우 중 가장 큰 값을 넓이 값으로 저장하기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def init(node, start, end):
    if start == end:
        tree[node] = (arr[start], start)
        return
    
    mid = (start + end)//2
    init(node*2, start, mid)
    init(node*2+1, mid+1, end)
    tree[node] = min(tree[2*node], tree[2*node+1])

def query(node, start, end, left, right):
    if right < start or end < left:
        return (1e9, 1e9)
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start+end)//2
    q1 = query(node*2, start, mid, left, right)
    q2 = query(node*2+1, mid+1, end, left, right)

    return min(q1, q2)

def get_area(left, right):
    minHeight, minIdx = query(1, 0, n-1, left, right)

    area = (right - left + 1)*minHeight
    
    if left < minIdx:
        val = get_area(left, minIdx - 1)
        area = max(area, val)

    if minIdx < right:
        val = get_area(minIdx + 1, right)
        area = max(area, val)
    
    return area

n = int(input())
arr = []
tree = [0] * (n*4)

for _ in range(n):
    arr.append(int(input()))

init(1, 0, n-1)
print(get_area(0, n-1))