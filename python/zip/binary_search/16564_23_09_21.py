# 히오스 프로게이머

# Min index를 저장하며 다음 값보다 작을 경우
# 가능한 만큼 증가시켜준다.
# 이 과정이 k > 0일 동안 반복한다.
# 시간초과
import sys

n, k = map(int, sys.stdin.readline().split())
levels = []
for _ in range(n):
    levels.append(int(sys.stdin.readline()))

levels.sort()
minCnt = 1
Min = 0
while k > 0:

    if Min >= n:
        Min = 1
        continue

    if levels[Min+1] == levels[Min]:
        minCnt += 1
    else:
        dif = levels[Min+1] - levels[Min]
        if minCnt == 1:
            if dif <= k: # 차이 만큼 증가할 수 있는 경우
                k -= dif
                minCnt += 1
                Min += 1
            elif dif == k: # 차이 만큼 증가하고, 끝이 나는 경우
                levels[Min] += dif
                break
            else: # 차이 만큼 증가할 수 없는 경우
                levels[Min] += k
                break
        else: # 최소가 여러 개인 경우
            if dif * minCnt < k: # 두 번째로 작은 수까지 증가할 수 있는 경우
                k -= dif * minCnt
                Min += 1
                minCnt += 1
            elif dif * minCnt == k: # 두 번째로 작은 수까지 증가하고 끝이 나는 경우
                levels[Min] += dif
                break
            else: # 두 번째로 작은 수까지 증가할 수 없는 경우
                levels[Min] += k // minCnt
                break
print(levels[Min])

# 이분 탐색

import sys

n, k = map(int, sys.stdin.readline().split())
levels = []
for _ in range(n):
    levels.append(int(sys.stdin.readline()))

levels.sort()
s = levels[0]
e = levels[-1] + k

while s <= e:
    mid = (s + e) // 2
    tmpK = 0

    for l in levels: # [10, 15, 20]
        if l < mid:
            tmpK += mid - l
            if tmpK > k:
                e = mid - 1
                break
    else: # k 안에 모든 수가 증가 가능한 것
        s = mid + 1

print(s-1)