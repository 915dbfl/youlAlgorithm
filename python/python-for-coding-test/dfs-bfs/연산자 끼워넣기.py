from itertools import permutations
import sys

n = int(input())
nums = list(map(int, input().split()))
cal_cnt = list(map(int, input().split()))
INF = sys.maxsize

cal_type = ["+", "-", "*", "%"]
cal = []
for i in range(4):
    for j in range(cal_cnt[i]):
        cal.append(cal_type[i])

def calculate(case):
    answer = nums[0]
    for i in range(len(case)):
        if case[i] ==  "+":
            answer += nums[i+1]
        elif case[i] == "-":
            answer -= nums[i+1]
        elif case[i] == "*":
            answer *= nums[i+1]
        else:
            if answer < 0:
                answer = -(-answer // nums[i+1])
            else:
                answer //= nums[i+1]

    return answer
        
Max, Min = -INF, INF
for case in permutations(cal, n-1):
    tmp_result = calculate(case)
    if Max < tmp_result:
        Max = tmp_result
    if Min > tmp_result:
        Min = tmp_result

print(Max)
print(Min)

# 예시 답안, dfs + 백트래킹

n = int(input())
# 연산을 수행하고자 하는 수 리스트
data = list(map(int, input().split()))
# 더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul, div = map(int, input().split())

# 최솟값과 최댓값 초기화
min_value = 1e9 # 10억
max_value = -1e9

# dfs 메서드
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i+1, now+data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now-data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now*data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now/data[i])) # 나눌 때는 나머지를 제거
            div += 1

# dfs 메서드 호출
dfs(1, data[0])

# 최댓값과 최솟값 차례대로 출력
print(max_value)
print(min_value)