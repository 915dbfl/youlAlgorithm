# 1시간
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

path = []
last_root = -1
def visit(target):
    global last_root
    path.append(target)
    if node[target][0] != -1 and not visited[node[target][0]]:
        visit(node[target][0])
        path.append(target)
    visited[target] = True
    last_root = target
    if node[target][1] != -1 and not visited[node[target][1]]:
        visit(node[target][1])
        path.append(target)

n = int(input())
node = [[0, 0] for _ in range(n+1)] # 왼쪽 자식, 오른쪽 자식, 부모
visited = [False] * (n+1)
for _ in range(n):
    a, b, c = map(int, input().split())
    node[a][0] = b
    node[a][1] = c

visit(1)
target = path[-1]
while target != last_root:
    path.pop()
    target = path[-1]
print(len(path) - 1)

# 다른 풀이
import sys
input = sys.stdin.readline

def dfs1(node):
    global count1
    visited[node] = True

    if tree[node][0] != -1 and not visited[tree[node][0]]:
        dfs1(tree[node][0])
        count1 += 1
    if tree[node][1] != -1 and not visited[tree[node][1]]:
        dfs1(tree[node][1])
        count1 += 1

def dfs2(node):
    global count2
    visited[node] = True

    if tree[node][1] != -1 and not visited[tree[node][1]]:
        dfs2(tree[node][1])
        count2 += 1

n = int(input())
tree = {}

for i in range(n):
    a, b, c = map(int, input().split())
    tree[a] = [b, c]

visited = [False] * (n+1)
count1 = 0
dfs1(1)
count2 = 0
visited = [False] * (n+1)
dfs2(1)

print(2*count1 - count2)