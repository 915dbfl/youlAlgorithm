# 배열에서 i-j까지 합을 구해야할 경우
# dp -> o(N), n이 클 경우 비효율
# segment_tree -> o(logN), 구간별 합을 저장해두는 방식

import sys
input = sys.stdin.readline

# 세그먼트 트리 생성
# node가 담당하는 구간 [start, end]
def init(node, start, end):
    # leaf일 경우
    if start == end:
        tree[node] = l[start]
        return tree[node]
    mid = (start + end)//2
    # 재귀를 통해 왼쪽 자식 및 오른쪽 자식의 합을 node에 저장
    tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
    return tree[node]
    
# 구간 합 구하기
# node가 담당하는 구간 [start, end]
# 합을 구해야 하는 구간 [left, right]
def subSum(node, start, end, left, right):
    
    # 요청 구간이 노드의 구간을 완전히 벗어나는 경우
    if left > end or right < start:
        return 0
    
    # 요청 구간이 노드의 구간을 완전히 포함하는 경우
    if left <= start and right >= end:
        return tree[node]

    # 노드의 구간이 요청 구간을 완전히 포함하는 경우 -> 절반으로 나눠 재귀 탐색
    mid = (start+end)//2 
    return subSum(node*2, start, mid, left, right) + subSum(node*2+1, mid+1, end, left, right)

def update(node, start, end, idx, diff):
    if idx < start or idx > end:
        return
    
    tree[node] += diff

    # 리프 노드가 아닌 경우에는 자식도 변경해주어야 한다.
    if start != end:
        mid = (start+end)//2
        update(node*2, start, mid, idx, diff)
        update(node*2+1, mid+1, end, idx, diff)

    

n, m, k = map(int, input().split())

l = []
tree = [0] * (n*4)

for _ in range(n):
    l.append(int(input()))

init(1, 0, n-1)

for _ in range(m+k):
    a, b, c = map(int, input().split())

    if a == 1:
        b = b-1
        diff = c - l[b]
        l[b] = c
        update(1, 0, n-1, b, diff)
    elif a == 2:
        print(subSum(1, 0, n-1, b-1, c-1))

# 참고 게시글: https://cheon2308.tistory.com/entry/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%84%B8%EA%B7%B8%EB%A8%BC%ED%8A%B8-%ED%8A%B8%EB%A6%ACSegment-Tree