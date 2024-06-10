# 17분
import sys
input = sys.stdin.readline

n = int(input())
days = [0] * 367
for _ in range(n):
    s, e = map(int, input().split())
    days[s] += 1
    days[e+1] -= 1

h, w = 0, 0
answer = 0
for i in range(1, 367):
    days[i] += days[i-1]
    if days[i] > 0:
        h = max(h, days[i])
        w += 1
    else:
        if h != 0 and w != 0:
            answer += h*w
            h, w = 0, 0

print(answer)