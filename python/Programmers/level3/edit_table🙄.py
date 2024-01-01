#22.07.14
#표 편집

# 내 풀이(효율성 통과 못함)
def solution(n, k, cmd):
    answer, lst = [], []
    for i in range(n):
        answer.append("X")
        lst.append(i)
    storage = []
    
    for str in cmd:
        if str == "C":
            storage.append((k, lst[k]))
            del lst[k]
            if k == len(lst):
                k-=1
        elif str == "Z":
            idx, val = storage.pop()
            lst.insert(idx, val)
            if idx <= k:
                k += 1
        else:
            c, a = str.split(" ")
            if c == "U":
                k -= int(a)
            elif c == "D":
                k += int(a)
    for i in lst:
        answer[i] = "O"
    return "".join(answer)

# 링크드리스트: 딕셔너리
def solution(n, k, cmd):
    table = {i: [i-1, i+1] for i in range(n)} # 더블링크드리스트처럼 양방향 노드에 대한 값을 가지고 있는다.
    table[0][0] = None
    table[n-1][1] = None
    answer = ["O"]*n
    storage = []
    cur = k
    
    for c in cmd:
        if c == "C": # 표에서 cur행을 삭제하고 다음 행을 가리키게 된다. 만약 cur이 마지막 행일 경우, 그 전 노드를 가르킨다.
            answer[cur] = "X"
            pre, next = table[cur]
            storage.append([pre, cur, next])
            if next == None: # 마지막 노드냐에 따라 cur을 업데이트한다.
                cur = pre
            else:
                cur = next
            if pre == None: # 인접 노드의 값들을 변경한다.
                table[next][0] = None
            elif next == None:
                table[pre][1] = None
            else:
                table[pre][1] = next
                table[next][0] = pre
        elif c == "Z":
            pre, idx, next = storage.pop() # 최근 삭제한 행에 대한 값을 가져온다.
            answer[idx] = "O"
            if pre == None: # 인접 노드의 값을 변경한다.
                table[next][0] = idx
            elif next == None:
                table[pre][1] = idx
            else:
                table[pre][1] = idx
                table[next][0] = idx 
        else:
            c1, c2 = c.split(" ")
            c2 = int(c2)
            if c1 == "U":
                for _ in range(c2):
                    cur = table[cur][0]
            else:
                for _ in range(c2):
                    cur = table[cur][1]
                    
    return "".join(answer)

# 링크드리스트: 클래스로 구현
class DoubleLinkedList:
    class Node:
        def __init__(self, num, pre):
            self.pre = pre
            self.num = num
            self.next = None
            
    def __init__(self, num, start):
        self.root = self.Node(0, None) # 없는 노드를 탐색하기 위해 root값 저장
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
        if remove_node.next:
            self.current = remove_node.next
            self.current.pre = remove_node.pre
            if remove_node == self.root:
                self.root = remove_node.next
            if remove_node.pre:
                remove_node.pre.next = self.current
        else:
            self.current = remove_node.pre
            self.current.next = None
            
    def recover(self):
        recover_node = self.stack.pop()
        if recover_node.pre:
            recover_node.pre.next = recover_node
        if recover_node.next:
            recover_node.next.pre = recover_node
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