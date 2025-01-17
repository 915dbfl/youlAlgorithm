"""
2시간 / 최적화 필요

[이진 트리를 어떻게 파악할 것인가?]
1. 자식 노드의 y값은 항상 부모 노드보다 작다
    - y순으로 정렬
    - y값이 가장 큰 값이 루트 노드 이다.
2. 부모 노드의 왼쪽/오른쪽 서브트리 속 노드들의 x값은 부모 노드의 x값보다 작다/크다.
    - x순으로 정렬
    - 루트 노드 탐색
    - 루트 노드를 기준으로 재귀 호출
"""
import sys
sys.setrecursionlimit(10**6)

prev = []
post = []

# 루트 노드의 위치를 알아내는 함수
def binary_search(s, e, target_x, list):
    start = s
    end = e
    
    while start <= end:
        mid = (start + end) // 2
        
        # x값으로 정렬 되어 있음
        # 따라서 x값에 따라 이분 탐색 진행
        if list[mid][1][0] == target_x:
            return mid
        elif list[mid][1][0] > target_x:
            end = mid-1
        elif list[mid][1][0] < target_x:
            start = mid +1
    return -1
            
# 루트 노드를 알아내는 함수
def find_root(node_rev_idx, start, end, node_rev_sorted_by_y, node_sorted_by_x):
    prev_root = node_rev_sorted_by_y[node_rev_idx]
    cur_root = node_rev_sorted_by_y[node_rev_idx+1]
    cur_root_idx = binary_search(start, end, cur_root[1][0], node_sorted_by_x)
    
    # y값으로 정렬된 배열에서 빠르게 루트 구하기
    while True:
        if cur_root[1][1] < prev_root[1][1] and start <= cur_root_idx <= end:
            break
        node_rev_idx += 1
        cur_root = node_rev_sorted_by_y[node_rev_idx]
        cur_root_idx = binary_search(start, end, cur_root[1][0], node_sorted_by_x)
        
    
    return cur_root, node_rev_idx, cur_root_idx

# 이진 트리 만들기
def make_tree(node_rev_idx, start, end, node_rev_sorted_by_y, node_sorted_by_x):
    
    # 범위를 넘어가거나 start > end일 경우 가지치기
    if start > end or start < 0 or end >= len(node_rev_sorted_by_y):
        return
    
    # 노드가 하나만 남을 때
    if start == end:
        prev.append(node_sorted_by_x[start][0])
        post.append(node_sorted_by_x[start][0])
        return
    
    # root 찾기
    root, nx_rev_idx, root_idx= find_root(node_rev_idx, start, end, node_rev_sorted_by_y, node_sorted_by_x)
    
    # 전위 추가
    prev.append(root[0])
    # 왼쪽 서브트리 탐색
    make_tree(nx_rev_idx, start, root_idx - 1, node_rev_sorted_by_y, node_sorted_by_x)
    # 오른쪽 서브트리 탐색
    make_tree(nx_rev_idx, root_idx + 1, end, node_rev_sorted_by_y, node_sorted_by_x)
    # 후위 추가
    post.append(root[0])
    
def solution(nodeinfo):
    node_with_index = list(map(lambda i: [i+1, nodeinfo[i]], range(len(nodeinfo))))
    node_rev_sorted_by_y = sorted(node_with_index, key = lambda x: (x[1][1], -x[1][0]), reverse = True)
    node_sorted_by_x= sorted(node_with_index, key = lambda x: x[1][0])
    
    root = node_rev_sorted_by_y[0]
    root_idx = binary_search(0, len(nodeinfo), root[1][0], node_sorted_by_x)
    prev.append(root[0])
    
    make_tree(0, 0, root_idx -1 , node_rev_sorted_by_y, node_sorted_by_x)
    make_tree(0, root_idx + 1, len(nodeinfo)-1, node_rev_sorted_by_y, node_sorted_by_x)
    post.append(root[0])
    return [prev, post]
    
    
# 트리를 만드는 과정에서 pre, post 구하기⭐️
# 핵심: root를 중심으로 left, right 나누며 재귀 진행

import sys
sys.setrecursionlimit(10**5)

def find_root(nodes):
    return max(nodes, key = lambda x: x[2])

def divide_nodes(nodes, sd):
    for i in range(len(nodes)):
        if nodes[i][1] == sd:
            return nodes[:i], nodes[i+1:]

def solution(nodeinfo):
    nodes = [(i+1, x, y) for i, (x, y) in enumerate(nodeinfo)]
    preOrder, postOrder = [], []
    
    def make_tree(nodes):
        if not nodes: return
        i, x, y = find_root(nodes)
        preOrder.append(i)
        x_nodes = sorted(nodes, key = lambda x: x[1])
        left_nodes, right_nodes = divide_nodes(x_nodes, x)
        make_tree(left_nodes)
        make_tree(right_nodes)
        postOrder.append(i)
        
    make_tree(nodes)
    
    return [preOrder, postOrder]

