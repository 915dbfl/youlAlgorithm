# 1시간 30분

from collections import defaultdict

values = [["" for _ in range(51)] for _ in range(51)]
parents = [[(i, j) for j in range(51)] for i in range(51)]

def getParent(x, y):
    px, py = parents[x][y]
    if (px, py) != (x, y):
        return getParent(px, py)
    return (px, py)

def solution(commands):

    childs = defaultdict(set)
    answer = []
    
    for command in commands:
        cmds = list(command.split())
        if cmds[0] == "UPDATE":
            if len(cmds) == 4:
                x, y, value = int(cmds[1]), int(cmds[2]), cmds[3]
                px, py = getParent(x, y)
                values[px][py] = value
            else:
                old, new = cmds[1:]
                # 추후 개선 필요
                for i in range(1, 51):
                    for j in range(1, 51):
                        if values[i][j] == old:
                            values[i][j] = new
        elif cmds[0] == "MERGE":
            r1, c1, r2, c2 = map(int, cmds[1:])
            px1, py1 = getParent(r1, c1)
            px2, py2 = getParent(r2, c2)
            
            # 서로 부모가 같지 않다면
            if px1 != px2 or py1 != py2:
                value = values[px1][py1] if values[px1][py1] != "" else values[px2][py2]
                # 부모 및 값 업데이트
                if px1 < px2 or py1 < py2:
                    parents[px2][py2] = (px1, py1)
                    childs[(px1, py1)] |= childs[(px2, py2)] | set([(px2, py2)])
                    values[px1][py1] = value
                else:
                    parents[px1][py1] = (px2, py2)
                    childs[(px2, py2)] |= childs[(px1, py1)] | set([(px1, py1)])
                    values[px2][py2] = value
        elif cmds[0] == "UNMERGE":
            # 부모 구하기
            r, c = map(int, cmds[1:])
            px, py = getParent(r, c)
            pval = values[px][py]
            values[px][py] = ""
            # 자식들 순회
            for child in childs[(px, py)]:
                cx, cy = child
                parents[cx][cy] = (cx, cy)
                values[cx][cy] = ""
                childs[(cx, cy)] = set() # 빼먹었음..
            childs[(px, py)] = set()
            # r, c 값 세팅
            values[r][c] = pval
        else: # print
            r, c = int(cmds[1]), int(cmds[2])
            pr, pc = getParent(r, c) # 빼먹었음..
            answer.append("EMPTY" if values[pr][pc] == "" else values[pr][pc])
    return answer