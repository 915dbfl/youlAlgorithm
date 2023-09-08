# 가장 긴 짝수 연속한 부분 수열

# 시간초과
# 현재 idx까지 짝수 순열의 개수
# 오른쪽에 홀수가 있는 짝수의 위치만 따로 분리
# 해당 위치에서 오른쪽으로 k개 제거해 얻을 수 있는 최대 부분 수열 구함
# -> 문제점 1
# 1 2 3 4 5 6의 경우, (1, 3)위치에서 최대 부분 수열을 구한다.
# 이때 수열의 최대 길이가 10**6이므로 10**12 반복하는 꼴!
s, k = map(int, input().split())
nums = list(map(int, input().split()))
dp = [0] * s
dp[0] = 1 if nums[0] % 2 == 0 else 0

for i in range(1, s):
    if nums[i] % 2 == 0:
        if nums[i-1] % 2 == 0:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = 1

case = []
if dp[-1] >= 1:
    case.append((dp[-1], s-1))
for i in range(s-1):
    if dp[i+1] == 0 and dp[i] >= 1:
        case.append((dp[i], i))

answer = 0
for cnt, idx in case:
    # 오른쪽 확인
    tmpI = idx+1
    tmpC = cnt
    rm = 0
    while 1:
        if rm > k:
            break
        if tmpI < s:
            if nums[tmpI] % 2 == 0:
                tmpC += 1
            else:
                rm += 1
            tmpI += 1
        else:
            break
    answer = max(answer, tmpC)

print(answer)

# 두 포인터
# p2
    # r이 k 이하일 경우 계속해서 앞으로 나아감
# p1
    # r이 k 초과가 되면 r의 개수를 -1하는 용도
# p2, p1이 바뀔때마다 짝수로만 이루어진 최대 부분 수열을 구한다.
n, k = map(int, input().split())
nums = list(map(int, input().split()))

p1 = p2 = 0
r = 0
answer = 0

while p2 < n:
    if nums[p2] % 2 == 0:
        p2 += 1
    else:
        r += 1
        p2 += 1
        if r > k:
            while 1:
                if nums[p1] % 2 == 0:
                    p1 += 1
                else:
                    p1 += 1
                    r -= 1
                    break
    answer = max(p2 - p1 - r, answer)

print(answer)