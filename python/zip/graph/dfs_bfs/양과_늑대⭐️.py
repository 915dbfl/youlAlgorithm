# dfs + backtracking
# 오늘의 교훈: dfs + backtracking이면 재귀를 생각해보자.

def solution(info, edges):
    visited = [0] * len(info)
    answer = []
    
    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return
        
        # 항상 모든 간선을 확인한다.
        for p, c in edges:
            if visited[p] and not visited[c]:
                visited[c] = 1
                if info[c] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[c] = 0
    
    visited[0] = 1
    dfs(1, 0)
    
    return max(answer)