# 뒤풀이 (35분)

"""
풀이과정
1. s는 준 술의 최댓값이다.
2. 모든 사람에게 준 술의 합은 t이다.
3. 이때 모든 사람은 s 이하의 술을 받는다.

s는 어떻게 구해야 할까?
(l보다는 무조건 커야 하니까 l 중에서는 최고를 선택해야 함)
(s이하이므로 r 중에서는 최고를 선택해야 함)
1. l의 최고 <= s <= r의 최고
2. 저 사이의 값에서 이분 탐색을 하게 된다면?
"""

import sys
input = sys.stdin.readline

n, t = map(int, input().split())
ranges = []

ss = 0
se = 0

def canAlloc(target):
    minAlloc = 0
    maxAlloc = 0

    for cl, cr in ranges:
        if target <= cr:
            maxAlloc += target
            minAlloc += cl
        else:
            maxAlloc += cr
            minAlloc += cl

    return minAlloc <= t <= maxAlloc

for _ in range(n):
    l, r = map(int, input().split())
    ranges.append([l, r])
    ss = max(ss, l)
    se = max(se, r)

# 이분탐색 진행
answer = sys.maxsize
while ss <= se:
    mid = (ss + se) // 2

    if canAlloc(mid):
        answer = min(answer, mid)
        se = mid - 1
    else:
        ss = mid + 1

print(-1 if answer == sys.maxsize else answer)