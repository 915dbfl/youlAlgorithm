# 시간 초과
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
# 4 * 4 * 4000 = 64KB
nums = [list(map(int, input().split())) for _ in range(n)]

# 4 + 4 (key - value) 쌍
# 딕셔너리 하나 용량: n^2 * 8 = 128MB
# 두 딕셔너리 용량: 256MB
prefix_dict1 = defaultdict(int)
for i in range(n):
    for j in range(n):
        prefix = nums[i][0] + nums[j][1]
        prefix_dict1[prefix] += 1

prefix_dict2 = defaultdict(int)
for i in range(n):
    for j in range(n):
        prefix = nums[i][2] + nums[j][3]
        prefix_dict2[prefix] += 1

answer = 0
for key in prefix_dict1:
    print(prefix_dict1[key],prefix_dict2[-key])
    answer += prefix_dict1[key] * prefix_dict2[-key]

print(answer)

# 투 포인터
# map은 매우 느림!
import sys
input = sys.stdin.readline

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

# 굳이 네 배열은 연속해서 더하지 않아도 된다!
# 4000 * 4000
prefix1 = []
prefix2 = []
for i in range(n):
    for j in range(n):
        prefix1.append(nums[i][0] + nums[j][1])
        prefix2.append(nums[i][2] + nums[j][3])
                
prefix1.sort()
prefix2.sort()

start, end = 0, len(prefix2)-1
result = 0
while start < len(prefix1) and end >= 0:
    if prefix1[start] + prefix2[end] == 0:
        nxtStart, nxtEnd = start + 1, end - 1
        while nxtStart < len(prefix1) and prefix1[start] == prefix1[nxtStart]:
            nxtStart += 1

        while nxtEnd >= 0 and prefix2[end] == prefix2[nxtEnd]:
            nxtEnd -= 1

        result += (nxtStart - start) * (end - nxtEnd)
        start, end = nxtStart, nxtEnd

    elif prefix1[start] + prefix2[end] > 0:
        end -= 1
    else:
        start += 1

print(result)