#뒤풀이
#이진탐색

#l의 최대값 - r의 최대값이 s가 될 수 있는 범위다.
#l의 총합이 t보다 클 때는 정확히 t가 될 수 없는 경우이므로 -1 출력
#r의 총합이 t보다 작을 때는 아무리해도 t가 될 수 없는 경우이므로 -1 출력
#위에서 구한 범위 내에서 이분탐색을 통해 최소 s 값을 구한다.
    # target값으로 모든 사람의 주량이 맞춰졌을 때 t 이상인지를 파악한다.

import sys
n, t = map(int, sys.stdin.readline().split())
cons = []
minM = maxM = 0
minC = maxC = 0

for _ in range(n):
    Min, Max = map(int, sys.stdin.readline().split())
    minC += Min
    maxC += Max
    minM = max(Min, minM)
    maxM = max(Max, maxM)
    cons.append([Min, Max])

if maxC < t or minC > t:
    print(-1)
    exit(0)

cons.sort()

def isValid(target):
    total = 0
    for i in range(n):
        if cons[i][1] >= target:
            total += target
        else:
            total += cons[i][1]

    if total >= t:
        return True
    else:
        return False

s, e = minM, maxM
mid = 0
while s <= e:
    mid = (s+e)//2

    if isValid(mid):
        e = mid - 1
    else:
        s = mid + 1

print(mid)