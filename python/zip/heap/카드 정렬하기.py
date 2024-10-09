import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
group = []

for i in range(n):
    heappush(group, int(input()))

answer = 0
while(len(group) > 1):
    g1 = heappop(group)
    g2 = heappop(group)

    answer += g1 + g2
    heappush(group, g1 + g2)

print(answer)