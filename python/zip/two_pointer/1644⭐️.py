# dp, 투 포인터
import sys

n = int(sys.stdin.readline())
nums = [True] * (n+1)
nums[0] = False; nums[1] = False

# 소수 판별
for i in range(2, int(n*0.5)+1):
    # 소수일 경우
    if nums[i]:
        # 에라토스테네스의 체 진행
        for j in range(i*2, n+1, i):
            nums[j] = nums[j] and False

# 소수합 dp에 저장
dp = [0]
sum = 0
for i in range(2, n):
    # 소수일 경우
    if nums[i]:
        sum += i
        dp.append(sum)

# 투 포인터 이용
p1, p2 = len(dp)-1, len(dp)-1
# n이 소수일 때 +1
cnt = 0
if nums[n]:
    cnt += 1
while 1:
    # 소수들의 합이 n보다 작을 경우 break
    if dp[p2] < n:
        break
    # 포인터 조정
    diff = dp[p2] - dp[p1]
    if diff >= n:
        if diff == n:
            cnt += 1
        p2 -= 1
    elif diff < n:
        p1 -= 1
print(cnt)