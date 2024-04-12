import sys
from collections import deque
input = sys.stdin.readline

# 틀린 풀이
# 반례: 1, 5, 2, 5, 9
# 정답: 0 / 오답: 1

n = int(input())
size = list(map(int, input().split()))
size.sort()

diff = []
for i in range(1, n):
    tmp = size[i] - size[i-1]
    diff.append([tmp, i-1, i])

# diff 차이가 작은 순으로 정렬
diff.sort(key = lambda x: x[0])

selected = set()
answer = 0
for d, s1, s2, in diff:
    if s1 not in selected and s2 not in selected:
        answer += d
        selected |= set([s1, s2])
    if len(selected) == 4:
        break

print(answer)

# 모든 경우의 수를 구해햐 함
# 오늘의 교훈: 시간을 초과하지 않는다면 모든 경우를 구하는 것도 생각해보자..
from itertools import combinations

n = int(input())
size = list(map(int, input().split()))
size.sort()

idx = [i for i in range(n)]

sum = []
# O(n^2)
for i1, i2, in combinations(idx, 2):
    sum.append([size[i1] + size[i2], set([i1, i2])])

sum.sort(key = lambda x: x[0])

answer = sys.maxsize
for i in range(1, len(sum)):
    snowman1 = sum[i]
    snowman2 = sum[i-1]

    if len(snowman1[1] & snowman2[1]) == 0:
        answer = min(answer, abs(snowman1[0] - snowman2[0]))

print(answer)

# 투포인터
# 미리 두 개의 원소를 선정하고
# 해당 원소들 사이에서 투 포인터를 통해
# 두 눈사람의 키 차이가 최소값이 되도록 한다.
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
# 지름 순으로 정렬
arr.sort()
ans = sys.maxsize

# 미리 두 원소 선정
for i in range(n):
    # i과 j 사이 원소 2개는 존재해야 함
    for j in range(i+3, n):
        # 원소사이 투 포인터 배치
        left = i+1
        right = j-1

        while left < right:
            tmp = (arr[i] + arr[j]) - (arr[left] + arr[right])
            ans = min(ans, abs(tmp))

            # tmp가 0보다 작다면
            # 키 차이를 줄이기 위해
            # tmp를 늘릴 필요 있으므로 right -= 1
            if tmp < 0:
                right -= 1
            # tmp가 0보다 크다면
            # 키 차이를 줄이기 위해
            # tmp를 줄일 필요 있으므로 left += 1
            else:
                left += 1

print(ans)
