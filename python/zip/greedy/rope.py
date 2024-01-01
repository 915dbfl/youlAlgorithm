#23.01.03
#로프
#알고리즘 스터디 3-2
#실버4

import sys
input = sys.stdin.readline

n = int(input())
ropes = [int(input()) for _ in range(n)]

ropes.sort()

answer = 0
for i in range(n):
  answer = max(answer, ropes[i]*(n-i))

print(answer)