#23.03.07
#최소비용 구하기2
#골드3

#다익스트라
import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
m = int(input())

bus = defaultdict(list)

def dijkstra1():
    h = [(s-1, 0)]
    result = [sys.maxsize] * n
    result[s-1] = 0

    while h:
        cur, cost = heappop(h)

        if cost > result[cur]:
            continue

        for next, val in bus[cur]:
            if result[next] > cost + val:
                result[next] = cost + val
                route[next] = route[cur] + [str(next+1)]
                heappush(h, (next, cost + val))
    
    return result

#경로를 저장하는 다른 방법: 포인터 사용
def dijkstra2():
    h = [(s-1, 0)]
    result = [sys.maxsize] * n
    result[s-1] = 0
    path = [-1 for _ in range(n)]

    while h:
        cur, cost = heappop(h)

        if cost > result[cur]:
            continue

        for next, val in bus[cur]:
            if result[next] > cost + val:
                result[next] = cost + val
                path[next] = cur+1
                heappush(h, (next, cost + val))
    
    return result[e-1], path

for _ in range(m):
    s, e, c = map(int, input().split())
    bus[s-1].append((e-1, c))

s, e = map(int, input().split())
# route = [[] for _ in range(n)]
# route[s-1].append(str(s))

# print(dijkstra1()[e-1])
# print(len(route[e-1]))
# print(" ".join(route[e-1]))


result, pointer = dijkstra2()
print(result, pointer)

path = [str(e)]
cur = e-1
while pointer[cur] != -1:
    path.append(str(pointer[cur]))
    cur = pointer[cur]-1
print(len(path))
print(" ".join(path[::-1]))