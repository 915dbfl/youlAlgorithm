#22.06.01
#네트워크

#내 풀이: dfs
def solution(n, computers):
    answer = 0
    l = len(computers)
    chk = [0 for _ in range(l)]
    que = []
    
    for j in range(l):
        if chk[j] != 1:
            que.append(j)
            while que:
                tmp = que.pop(0)
                if chk[tmp] == 0:
                    for i in range(l):
                        if computers[tmp][i] == 1:
                            que.append(i)
                    chk[tmp] = 1
            answer += 1
    return answer