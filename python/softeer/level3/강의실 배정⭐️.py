# list로 할 경우 sort하는 과정에서 시간 초과
# 정렬하는 과정을 없애기 위해 heapq 사용

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    # 종료 시간을 기준으로 정렬
    heappush(arr, (b, a))

answer = 0
now = 0

while arr:
    a, b = heappop(arr)
    # 시작시간이 이전 종료시간보다 늦다면
    if b >= now:
        now = a # 새로운 종료시간 업데이트
        answer += 1
print(answer)