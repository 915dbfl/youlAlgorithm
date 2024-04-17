# 누적합 활용
# dp[i] % k값을 활용해 nC2를 할 경우
# 음수와 양수관련 처리를 해줘야 함.
# dp[i - k*i를 할 경우 굳이 음수와 양수를 나눠 처리하지 않아도 됨.

import sys
from collections import defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))
dp = [0] 

for i in range(n):
    dp.append(dp[-1] + nums[i])

difflist = [0] * (n+1)
for i in range(n+1):
    difflist[i] = dp[i] - k*i

diffdict = defaultdict(int)
for i in range(n+1):
    d = difflist[i]
    diffdict[d] += 1

result = 0
for d in diffdict:
    cnt = diffdict[d]
    result += cnt*(cnt-1)//2

print(result)

# 누적합 활용
# 오답
# 평균이 음수더라도 양수 평균에 대해 count를 함
import sys
from collections import defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))
dp = [0]

for i in range(1, n):
    dp.append(dp[i-1] + nums[i])

dic = defaultdict(int)
for i in range(n):
    if k == 0:
        dic[dp[i]] += 1
    else:
        if (k < 0 and dp[i] <= 0) or (k > 0 and dp[i] >= 0):
            dic[dp[i] % k] += 1

answer = 0
for k in dic.keys():
    answer += (dic[k] * (dic[k] - 1)) // 2

print(answer)