import sys
input = sys.stdin.readline

n, m = map(int, input().split())
weights = list(map(int, input().split()))

best = [True] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    if weights[a-1] > weights[b-1]:
        best[a] = best[a] & True
        best[b] = best[b] & False
    elif weights[a-1] == weights[b-1]:
        best[a] = best[a] & False
        best[b] = best[b] & False
    else:
        best[a] = best[a] & False
        best[b] = best[b] & True
    
answer = 0
for i in range(1, n+1):
    if best[i]:
        answer += 1
print(answer)