import sys
input = sys.stdin.readline

def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]
    
def union(a, b):
    parentA = find_parent(a)
    parentB = find_parent(b)
    if parentA < parentB:
        parent[parentB] = parentA
    else:
        parent[parentA] = parentB

        
t = int(input())
for i in range(1, t+1):

    n = int(input())
    k = int(input())
    parent = [i for i in range(n)] 

    for _ in range(k):
        a, b = map(int, input().split())
        if find_parent(a) != find_parent(b):
            union(a, b)

    m = int(input())

    print('Scenario '+str(i)+':')

    for _ in range(1, m+1):
        u, v = map(int, input().split())
        if find_parent(u) == find_parent(v):
            print(1)
        else:
            print(0)

    print()
