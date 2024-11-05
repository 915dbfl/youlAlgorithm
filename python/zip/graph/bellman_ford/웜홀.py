# 1시간
import sys
input = sys.stdin.readline

def bellmanFord(n, edges):
    dist = [0] * (n+1)

    for i in range(n):
        for s, e, t in edges:
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                if i == n-1:
                    return True
    return False

tc = int(input())

for _ in range(tc):
    n, m, w= map(int, input().split())
    edges = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    if bellmanFord(n, edges):
        print("YES")
    else:
        print("NO")