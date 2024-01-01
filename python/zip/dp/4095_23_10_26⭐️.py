# 최대 정사각형

# 오답
import sys

def rowCheck(x, y):
    while 1:
        if x >= 0 and y >= 0:
            if row[x][y] != 0:
                x -= 1
                y -= 1
                continue
            else:
                return False
        else:
            return True


def colCheck(x, y):
    while 1:
        if x >= 0 and y >= 0:
            if col[x][y] != 0:
                x -= 1
                y -= 1
                continue
            else:
                return False
        else:
            return True

while (1):
    n, m = map(int, sys.stdin.readline().split())
    if n + m == 0:
        exit(0)
    else:
        graph = []
        for _ in range(n):
            graph.append(list(map(int, sys.stdin.readline().split())))

        row = [[0] * m for _ in range(n)]
        col = [[0] * m for _ in range(n)]
        for i in range(m):
            col[0][i] = graph[0][i]

        for j in range(n):
            row[j][0] = graph[j][0]
        
        # row 구하기
        for i in range(n):
            for j in range(1, m):
                if graph[i][j] == 1:
                    row[i][j] = row[i][j-1] + 1
                
        # col 구하기
        for i in range(1, n):
            for j in range(m):
                if graph[i][j] == 1:
                    col[i][j] = col[i-1][j] + 1

        # check
        result = 0
        rowCheckV = False
        colCheckV = False
        for i in range(n):
            for j in range(m):
                tmpR = min(row[i][j], col[i][j])
                if result < tmpR:
                    rowCheckV = False
                    colCheckV = False
                    if row[i][j] != 0:
                        rowCheckV = rowCheck(i-1, j-1)
                    if col[i][j] != 0:
                        colCheckV = colCheck(i-1, j-1)
                    
                    if rowCheckV & colCheckV:
                        if result < tmpR:
                            result = tmpR
        print(result)

# 다른 풀이: dp
# dp에 저장되는 값: 해당 위치가 정사각형의 오른쪽 꼭짓점일 때 최대 정사각형의 너비값
# 위, 왼, 대각선 위 중 최소값을 선택해 + 1을 진행한다.
    # 최소값을 선택해야 나머지 방향에는 1이 있다는 보장이 되기 때문이다.
import sys

while 1:
    n, m = map(int, sys.stdin.readline().split())
    if n + m == 0:
        break

    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))

    dp = [[0] * m for _ in range(n)]
    for i in range(m):
        dp[0][i] = graph[0][i]

    for i in range(n):
        dp[i][0] = graph[i][0]

    for i in range(1, n):
        for j in range(1, m):
            if graph[i][j] == 1:
                Min = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                dp[i][j] = Min+1
    
    result = 0
    for i in range(n):
        Max = max(dp[i])
        if result < Max:
            result = Max
    
    print(result)