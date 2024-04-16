# 최소 스패닝 트리
# 하나의 트리를 만들기 위해서
# 사이클이 존재하면 끊기
# 부모가 서로 다르면 연결하기
# 23분

import sys
input = sys.stdin.readline

def find_parent(a):
    if parent[a] == a: return a
    else: 
        parent[a] = find_parent(parent[a])
        return parent[a]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n, m = map(int, input().split())
connected = []
parent = [i for i in range(n+1)]
answer = 0

# 시냅스 정보 받아오기
for _ in range(m):
    u, v = map(int, input().split())
    pu, pv = find_parent(u), find_parent(v)

    # 연결을 끊어야 하는지 확인
    if (pu == pv):
        answer += 1
    # 시냅스 연결로 parent값 업데이트
    elif pu != pv:
        union(u, v)

# 서로 다른 부모 받아오기
parent_lst = set()
for i in range(1, n+1):
    parent_lst.add(find_parent(i))

# n명의 부모를 연결하기 위해서는 최소 n-1개의 시냅스가 필요하다
answer += len(parent_lst) - 1
print(answer)