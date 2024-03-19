import sys
sys.setrecursionlimit(10**4)

class BinaryTree:
    def __init__(self, nodes):
        # 지금까지 완성된 트리
        clear = Node(nodes[0][2], nodes[0][0], nodes[0][1])
        self.root = clear
        new = None
    
        for idx in range(1, len(nodes)):
            new = Node(nodes[idx][2], nodes[idx][0], nodes[idx][1])
            # new가 clear의 right인지 판단
            if clear.y >= new.y:
                # new의 y값보다 작은 값이 나올 때까지 child 탐색
                cur = clear
                while cur.right != None and cur.right.y > new.y:
                    cur = cur.right
                # new 추가
                new.left = cur.right
                cur.right = new
                
            # clear가 new의 left인지 판단
            else:
                new.left = clear
                clear = new
                
            # root 업데이트
            if self.root.y < new.y:
                self.root = new
            
class Node:
    def __init__(self, num, x, y):
        self.num = num
        self.x = x
        self.y = y
        self.left = None
        self.right = None
        
# 전위 순회 함수        
def getPre(cur):
    order = []
    if cur.left == None and cur.right == Node:
        return [cur.num]
    else:
        order.append(cur.num)
        if cur.left != None:
            leftChild = getPre(cur.left)
            for c in leftChild:
                order.append(c)
        if cur.right != None:
            rightChild = getPre(cur.right)
            for c in rightChild:
                order.append(c)
                
    return order
    
# 후위 순회 함수    
def getPost(cur):
    order = []
    if cur.left != None:
        leftChild = getPost(cur.left)
        for c in leftChild:
            order.append(c)
    if cur.right != None:
        rightChild = getPost(cur.right)
        for c in rightChild:
            order.append(c)
    order.append(cur.num)

    return order
         
def solution(nodeinfo):
    # num과 node 함께 관리
    nodeinfo = [[nodeinfo[idx][0], nodeinfo[idx][1], idx+1] for idx in range(len(nodeinfo))]
    # 노드 위치 파악을 위한 정렬
    nodeinfo.sort(key = lambda x: (x[0]))
    # 이진 트리 생성
    tree = BinaryTree(nodeinfo)
    # 전위 순회
    answer = []
    answer.append(getPre(tree.root))
    answer.append(getPost(tree.root))
    
    return answer
    
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