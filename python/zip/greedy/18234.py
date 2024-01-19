# 그리디, 정렬
import sys
input = sys.stdin.readline

n, t= map(int, input().split())

carrot = []
for _ in range(n):
    carrot.append(list(map(int, input().split())))

carrot.sort(key = lambda x: (x[1], [0]), reverse=True)

day = t
answer = 0
for c in carrot:
    answer += c[0] + (c[1] * (day - 1))
    day -= 1

print(answer)