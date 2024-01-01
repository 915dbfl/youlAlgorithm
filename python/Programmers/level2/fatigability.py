#22.04.16
#피로도

#내 풀이
from itertools import permutations

def solution(k, dungeons):
    answer = set()
    for case in permutations(dungeons):
        tmp = k
        cnt = 0
        for i in case:
            if tmp >= i[0]:
                tmp -= i[1]
                cnt += 1
            else:
                answer.add(cnt)
                break
        else:
            answer.add(cnt)
    return max(answer)

# dfs 풀이
def dfs(k, cnt, dungeons):
    global answer, visited
    if cnt > answer:
        answer = cnt
        
    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and not visited[i]:
            visited[i] = 1
            dfs(k-dungeons[i][1], cnt+1, dungeons)
            # visited을 다시 0으로 셋팅해 모든 순서의 경우를 고려할 수 있게 됨.
            visited[i] = 0
                   
def solution(k, dungeons):
    global visited, answer
    visited = [0] * len(dungeons)
    answer = 0
    dfs(k, 0, dungeons)
    return answer

# 던전 효율성 계산
def solution(k, dungeons):
    answer = 0
    #효율성: 최소 피로도와 비례, 소모 피로도와 반비례
    dungeons.sort(key = lambda x: (x[1]/x[0], x[1]))
    for x, y in dungeons:
        if k >= x:
            k -= y
            answer += 1
    return answer