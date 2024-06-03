# 30분

# 백트래킹: python3로 했을 때 시간초과
# 시간복잡도: (m+1)^n
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
p, m = map(int, input().split())

result = 0

def cal(group):
    answer = 1
    for g in group:
        if len(g) == 0:
            return 0
        answer *= sum(g)

    return answer

def dfs(group, target):
    global result
    if target == n:
        result = max(result, cal(group))
        return 
    
    num = nums[target]
    for i in range(m+1):
        group[i].append(num)
        dfs(group, target+1)
        group[i].pop()

# 수들의 합을 m+1개로 균등 분배
group = [[] for _ in range(m+1)]
dfs(group, 0)
print(result)

# combination 사용 다른 풀이
# combination 구하는 식: k= (1~n) nCk값 더하기
# 시간 복잡도: m*2^n
from itertools import combinations

def dfs(cu_val, cnt, pick_list):
    global result
    # 곱셈 기호가 더 이상 없을 때
    if cnt == 0:
        result = max(result, cu_val * sum(pick_list))
        return
    else:
        # 남아있는 숫자들의 index 배열 구하기
        idx_list = range(len(pick_list))
        # 곱셈 사이 숫자는 적어도 1개 이상이어야 하므로
        # 뽑을 수 있는 숫자의 개수에서 cnt 빼기
        for pick_cnt in range(1, len(pick_list) - cnt+1):
            for comb in combinations(idx_list, pick_cnt):
                copy_pick_list = pick_list[:]
                # pop을 했을 때 앞 인덱스의 값에 영향이 없도록 index가 큰 수부터 pop 진행
                comb = list(reversed(comb))
                temp_sum = 0
                for idx in comb:
                    temp_sum += copy_pick_list.pop(idx)
                dfs(cu_val * temp_sum, cnt - 1, copy_pick_list)

n = int(input())
nums = list(map(int, input().split()))
p, m = map(int, input().split())
result = 0
dfs(1, m, nums)
print(result)