class DoubleLinkedList:
    class Node:
        def __init__(self, num, pre):
            self.pre = pre
            self.num = num
            self.next = None
    
    # root, current, stack
    def __init__(self, num, start):
        self.root = self.Node(0, None)
        self.current = None
        self.stack = []
        temp = self.root
        for i in range(1, num):
            new_node = self.Node(i, temp)
            temp.next = new_node
            if i == start:
                self.current = new_node
            temp = new_node
    
    def up(self, num):
        for _ in range(num):
            self.current = self.current.pre
            
    def down(self, num):
        for _ in range(num):
            self.current = self.current.next
            
    def remove(self):
        remove_node = self.current
        self.stack.append(remove_node)
        
        # 마지막 노드가 아닌 경우
        if remove_node.next:
            # 현재 값 업데이트
            self.current = remove_node.next
            self.current.pre = remove_node.pre
            
            # 삭제한 값이 root라면
            if remove_node == self.root:
                self.root = remove_node.next
                
            # 삭제한 이전 값 next 변경
            if remove_node.pre:
                remove_node.pre.next = self.current
        
        # 마지막 노드일 경우
        else:
            self.current = remove_node.pre
            self.current.next = None
            
    def recover(self):
        recover_node = self.stack.pop()
        
        # pre 복구
        if recover_node.pre:
            recover_node.pre.next = recover_node
            
        # next 복구
        if recover_node.next:
            recover_node.next.pre = recover_node
            
            # 만약 recover_node.next가 root라면
            if recover_node.next == self.root:
                self.root = recover_node
    
    def get_root(self):
        return self.root

            
def solution(n, k, cmd):
    table = DoubleLinkedList(n, k)
    for c in cmd:
        if c == "C":
            table.remove()
        elif c == "Z":
            table.recover()
        else:
            c1, c2 = c.split(" ")
            c2 = int(c2)
            if c1 == "U":
                table.up(c2)
            else:
                table.down(c2)
    node = table.get_root()
    result = ["X"]*n
    while node:
        result[node.num] = "O"
        node = node.next
    return "".join(result)