# 1시간 10분

"""
풀이과정
1. 점수 따기 -> 어피치보다 1발만 더 쏘면 됨
2. 점수 잃기 -> 한 발도 쏘지 않으면 됨
"""
def solution(n, info):
    lion_info = [0] * 11
    
    diff_score = -1
    answer = [0] * 11
    
    def cal_score():
        apeach = 0
        lion = 0
        
        for i in range(11):
            score = 10 - i
            # 둘 다 점수를 갖지 못하는 경우
            if info[i] == 0 and lion_info[i] == 0: 
                continue
            
            # 어피치가 이기는 경우
            if info[i] >= lion_info[i]:
                apeach += score
            # 라이언이 이기는 경우
            else:
                lion += score
                
        return [apeach < lion, lion - apeach]
        
    def update_result(cur_diff):
        nonlocal diff_score, answer
        # 차이가 더 클 경우 바로 업데이트
        if cur_diff > diff_score:
            diff_score = cur_diff
            answer = lion_info[:]
        # 차이가 동일할 경우, 낮은 점수를 더 많이 쏜 경우로 업데이트
        elif cur_diff == diff_score:
            need_update = False
            for i in range(10, -1, -1):
                if answer[i] < lion_info[i]:
                    need_update = True
                    break
                elif answer[i] > lion_info[i]: # 놓쳤던 조건문⭐️
                    break
            if need_update:
                answer = lion_info[:]
            
    def dfs(cur_idx, left):
        # 마지막인 경우
        if cur_idx == 10 or left == 0:

            # 남은 화살 처리
            lion_info[10] = left
            # 승 여부, 점수 차이
            result = cal_score()
            if result[0]:
                update_result(result[1])
            # backtracking
            lion_info[10] = 0
            return
        
        # 점수를 딸 수 있다면
        if left >= info[cur_idx] + 1:
            shoot = info[cur_idx] + 1
            lion_info[cur_idx] = shoot
            dfs(cur_idx+1, left - shoot)
            lion_info[cur_idx] = 0
        
        dfs(cur_idx+1, left)
        
    dfs(0, n)
    
    if sum(answer) == n:
        return answer
    else:
        return [-1]
    
# 더 느린 풀이 + 깔끔한 코드

def solution(n, info):
    answer = [0 for _ in range(11)]
    result = 0

    def score(ryan):
        s = 0
        for i in range(11):
            if ryan[i] == info[i] == 0:
                continue
            if ryan[i] > info[i]:
                s += 10 - i
            else:
                s -= 10 - i
        return s

    def dfs(idx, left, ryan):
        nonlocal answer, result
        if idx == -1 and left:
            return
        if left == 0:
            s = score(ryan)
            if result < s:
                answer = ryan[:]
                result = s
            return
        # 모든 경우의 수 파악
        for i in range(left, -1, -1):
            ryan[idx] = i
            dfs(idx-1, left-i, ryan)
            ryan[idx] = 0


    dfs(10, n, [0 for _ in range(11)])
    return answer if result != 0 else [-1]