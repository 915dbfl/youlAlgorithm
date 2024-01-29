# 투포인터
import sys
input = sys.stdin.readline

n = int(input())
type = list(map(int, input().split()))
type.sort()

p1, p2 = 0, n-1
result = 200000001

while p1 < p2:
    new_type = type[p1] + type[p2]
    if new_type >= 0:
        p2 -= 1
    else:
        p1 += 1
    
    if abs(0-result) > abs(0-new_type):
        result = new_type

print(result)