# 표 병합

# 다른 풀이: 단순 구현
def solution(commands):
    answer = []
    merged = [[(i, j) for j in range(50)] for i in range(50)]
    board = [["EMPTY"]* 50 for _ in range(50)]

    for command in commands:
        command = command.split(" ")
        if command[0] == 'UPDATE':
            if len(command) == 4:
                r,c,value = int(command[1])-1,int(command[2])-1,command[3]
                x,y = merged[r][c]
                board[x][y] = value
            elif len(command) == 3:
                value1, value2 = command[1], command[2]
                for i in range(50):
                    for j in range(50):
                        if board[i][j] == value1:
                            board[i][j] = value2
        elif command[0] == "MERGE":
            r1,c1,r2,c2 = int(command[1])-1, int(command[2])-1, int(command[3])-1, int(command[4])-1
            x1,y1 = merged[r1][c1]
            x2, y2 = merged[r2][c2]
            if board[x1][y1] == "EMPTY":
                board[x1][y1] = board[x2][y2]
            for i in range(50):
                for j in range(50):
                    if merged[i][j] == (x2, y2):
                        merged[i][j] = (x1, y1)
        elif command[0] == "UNMERGE":
            r, c = int(command[1])-1, int(command[2])-1
            x, y = merged[r][c]
            tmp = board[x][y]
            for i in range(50):
                for j in range(50):
                    if merged[i][j] == (x, y):
                        merged[i][j] = (i, j)
                        board[i][j] = "EMPTY"
            board[r][c] = tmp
        elif command[0] == "PRINT":
            r, c = int(command[1])-1, int(command[2])-1
            x, y = merged[r][c]
            answer.append(board[x][y])

    return answer

# union - find 적용
# parent의 parent가 가지고 있는 값이 실제 자식이 가지고 있는 값이 된다.
# merge
    # merge하려고 하는 두 요소의 부모를 같게 만든다.
    # 만약 부모셀 중 왼쪽 셀이 empty라면 오른쪽 셀의 값으로
    # 아니라면 왼쪽 셀의 값으로 통일한다.
# unmerge
    # 부모셀의 값을 가지고 있는 모든 셀을 구해 초기화를 시켜준다.
parent = [[(r, c) for c in range(51)] for r in range(51)]
cells = [["EMPTY"] * 51 for _ in range(51)]
result = []

def find(r, c):
    if (r, c) == parent[r][c]:
        return parent[r][c]
    pr, pc = parent[r][c]
    parent[r][c] = find(pr, pc)
    return parent[r][c]

def union(r1, c1, r2, c2):
    parent[r2][c2] = parent[r1][c1]

def update(r, c, msg):
    pr, pc = find(r, c)
    cells[pr][pc] = msg

def update_val(msg1, msg2):
    for r in range(51):
        for c in range(51):
            pr, pc = find(r, c)
            if cells[pr][pc] == msg1:
                cells[pr][pc] = msg2

def merge(r1, c1, r2, c2):
    r1, c1 = find(r1, c1)
    r2, c2 = find(r2, c2)

    if (r1, c1) == (r2, c2):
        return
    if cells[r1][c1] != "EMPTY":
        union(r1, c1, r2, c2)
    else:
        union(r2, c2, r1, c1)

def unmerge(r, c):
    pr, pc = find(r, c)
    msg = cells[pr][pc]

    for ar in range(51):
        for ac in range(51):
            apr, apc = find(ar, ac)
            if (apr, apc) == (pr, pc):
                parent[apr][apc] = (apr, apc)
                cells[apr][apc] = "EMPTY" if (apr, apc) != (r, c) else msg

def print(r, c):
    pr, pc = find(r, c)
    result.append(cells[pr][pc])