# 누적합

import sys
input = sys.stdin.readline

brackets = list(input().rstrip())
dp = [0] * len(brackets)
dp[0] = 1 if brackets[0] == "(" else -1

for i in range(1, len(brackets)):
    if brackets[i] == "(":
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = dp[i-1] - 1

minusL = [0] * len(brackets)
minusR = [0] * len(brackets)
# 0 미만인 dp 개수 모두 count
minusL[0] = 1 if dp[0] < 0 else 0
# 1 이하인 dp 개수 모두 count
minusR[-1] = 1 if dp[-1] <= 1 else 0

for i in range(1, len(brackets)):
    if dp[i] < 0:
        minusL[i] = minusL[i-1] + 1
    else:
        minusL[i] = minusL[i-1]

for i in range(len(brackets)-2, -1, -1):
    if dp[i] <= 1:
        minusR[i] = minusR[i+1] + 1
    else:
        minusR[i] = minusR[i+1]

answer = 0
for i in range(len(brackets)):
    # ( -> ): -2 진행
    if brackets[i] == "(":
         # 이미 앞에서 올바르지 않은 괄호가 존재하는 경우
        if minusL[i] > 0: continue

        if  minusR[i] == 0 and dp[-1] - 2 == 0:
            answer += 1

    # ) -> (: +2 진행
    else:
        if dp[i] + 2 < 0: continue
        if i > 0 and minusL[i-1] > 0: continue

        if dp[-1] + 2 == 0:
            answer += 1

print(answer)

# 다른 풀이
# 오탈자가 한 개만 존재하는 것이 핵심!
# 오탈자가 존재할 수 밖에 없는 영역이 나오면 뒤에 있는 것은 고려하지 않아도 된다. (뒤에는 오탈자가 없어야 하므로)
brackets = list(input())

cnt, l_cnt, r_cnt = 0, 0, 0

for bracket in brackets:
    if bracket == "(":
        l_cnt += 1
        cnt += 1
    else:
        r_cnt += 1
        cnt -= 1

    # '(('일 경우에 경우의 수는 1
    # 따라서 l_cnt를 cnt - 1로 초기화
    if cnt == 1:
        l_cnt = 0
    
    # 오탈자가 존재할 수 밖에 없음!
    # ')'가 무조건 오탈자 -> 따라서 ')'개수 만큼 경우의 수가 존재
    if cnt == -1:
        print(r_cnt)
        exit(0)

# ')'로 오탈자가 발생하지 않았다면 -> '('로 오탈자 발생
# 오탈자가 한 개만 존재하므로 '('로 오탈자가 발생할 경우 cnt == 2
if cnt == 2:
    print(l_cnt)
# cnt == 2가 아니라면 ')', '(' 모두 오탈자가 발생하지 않음!
else:
    print(0)