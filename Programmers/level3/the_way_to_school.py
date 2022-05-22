#22.05.23
#등굣길

#내 풀이: 동적 계획법 사용
def solution(m, n, puddles):
    ways = [[0]*m for _ in range(n)]
    ways[0][0] = 1

    for i in range(n):
        for j in range(m):
            try:
                if [j+1, i] not in puddles:
                    ways[i][j] += ways[i-1][j]
                if [j, i+1] not in puddles:
                    ways[i][j] += ways[i][j-1]
            except:
                continue
    return ways[n-1][m-1] % 1000000007

#재귀 풀이
def solution(m, n, puddles):
    dic = dict([((2, 1), 1), ((1, 2), 1)])
    for p in puddles:
        dic[tuple(p)] = 0
        
    def func(m, n):
        if m < 1 or n < 1:
            return 0
        if (m, n) in puddles:
            return dic[(m, n)]
        return dic.setdefault((m, n), func(m-1, n) + func(m, n-1))

    return func(m, n) % 1000000007