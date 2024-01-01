# 이분 그래프

# 접근: 사이클이 없다면 이분 그래프에 해당한다.
# 이분 그래프: 연결된 정점을 서로 다른 색으로 칠할 때, 단 두개의 색으로 그래프가 칠해질 경우 해당 그래프를 이분 그래프라고 한다.
# 각 간선은 양방향으로 생각한다. 
# 서클이 존재하는지를 확인한다.
    # 바로 이전에 방문한 정점은 별도로 저장해
    # 서클인지 아닌지 확인하는 데 사용한다.

# 해당 풀이가 틀린 이유: 단순 서클이 만들어진다고 해서 이분 그래프가 아니라도 가정할 수 없다.
    # 사이클이 만들어졌어도 단 두개의 색으로 그래프가 칠해질 경우가 있기 때문

import sys
from collections import defaultdict, deque

k = int(sys.stdin.readline())
for _ in range(k):
    v, e = map(int, sys.stdin.readline().split())
    dic = defaultdict(list)
    
    for _ in range(e):
        s, e = map(int, sys.stdin.readline().split())
        dic[s].append(e)
        dic[e].append(s)

    keys = list(dic.keys())
    dq = deque([keys[0]])
    visited = [0] * (v+1)
    before = -1
    checkDone = False

    while dq:
        cur = dq.popleft()
        visited[cur] = 1

        for n in dic[cur]:
            if visited[n] == 1: # 한 번 방문한 노드
                if n != before: # 바로 이전에 방문한 노드가 아닐 경우, 사이클에 해당
                    print("NO")
                    checkDone = True
                    break
            else:
                before = cur
                dq.append(n)
        if checkDone:
            break
    
    # 모든 정점 확인, 사이클이 없을 때
    if not checkDone:
        print("YES")

# 시간 초과
# 각 정점의 값을 0과 1로 저장한다.
# 서로 인접한 정점이 서로 다른 값이 된다면 이분 그래프이다.
import sys
from collections import defaultdict, deque

k = int(sys.stdin.readline())
for _ in range(k):
    v, e = map(int, sys.stdin.readline().split())
    dic = defaultdict(list)
    
    for _ in range(e):
        s, e = map(int, sys.stdin.readline().split())
        dic[s].append(e)
        dic[e].append(s)

    keys = list(dic.keys())
    dq = deque([(keys[0], 0)])
    visited = [-1] * (v+1)
    checkDone = False

    while dq:
        cur, val = dq.popleft()
        visited[cur] = val

        for n in dic[cur]:
            if visited[n] != -1: # 이전에 방문한 노드
                if visited[n] == val: # 인접한 노드를 서로 다른 집합에 넣을 수 없는 경우
                    print("NO")
                    checkDone = True
                    break
            else:
                nxtValue = (val + 1) % 2
                dq.append((n, nxtValue))
        if checkDone:
            break

    # 모든 정점 확인, 사이클이 없을 때
    if not checkDone:
        print("YES")

# 다른 풀이

import sys
from collections import deque

input = sys.stdin.readline


# bfs
def bfs(start, group):
    queue = deque([start])  # 시작 정점 값을 큐에 담는다.
    visited[start] = group  # 시작 정점 그룹을 설정
    while queue:  # 큐가 존재할때까지 돈다.

        x = queue.popleft()  # 큐의 맨앞 원소를 빼낸다.

        for i in graph[x]:  # 해당 정점에서 갈 수 있는 하위 정점들을 돈다.
            if not visited[i]:  # 만약 그 정점들을 아직 방문하지 않았다면
                queue.append(i)  # 그 정점들을 추가하고
                visited[i] = -1 * visited[x]  # 상위 정점과 다른 그룹으로 편성
            elif visited[i] == visited[x]:  # 만약 정점들을 이미 방문했었는데 같은 그룹이라면
                return False  # False를 바로 리턴
    return True  # 위의 조건에 걸리지 않았다면 True를 리턴


for _ in range(int(input())):
    V, E = map(int, input().split())
    graph = [[] for i in range(V + 1)]  # 빈 그래프 생성
    visited = [False] * (V + 1)  # 방문한 정점 체크

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)  # 무방향 그래프
        graph[b].append(a)  # 무방향 그래프

    for i in range(1, V + 1):
        if not visited[i]:  # 방문한 정점이 아니면, bfs 수행
            result = bfs(i, 1)
            if not result:
                break

    print('YES' if result else 'NO')