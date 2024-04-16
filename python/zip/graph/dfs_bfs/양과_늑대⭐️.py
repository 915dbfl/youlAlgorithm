# dfs + backtracking
# 오늘의 교훈: dfs + backtracking이면 재귀를 생각해보자.

def solution(info, edges):
    answer = 0
    visited = [0] * len(info)
    visited[0] = 1
    
    def dfs(cur, sheep, wolf):
        nonlocal answer
        if sheep > wolf:
            answer = max(sheep, answer)
        else:
            return
        
        # 연결 가능한 모든 간선을 확인하기 위해
        # 매단계 모든 간선 확인
        for a, b in edges:
            # 현재와 연결할 수 있는 모든 간선 확인
            # 부모가 이미 방문 완료되었고, 자식이 아직 방문되지 않았을 경우
            if visited[a] == 1 and visited[b] != 1:
                visited[b] = 1
                # 양, 늑대 개수 적절히 업데이트
                if info[b] == 0:
                    dfs(b, sheep+1, wolf)
                else:
                    dfs(b, sheep, wolf+1)
                visited[b] = 0
                    
    dfs(0, 1, 0)
    return answer