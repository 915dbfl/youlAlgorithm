#22.06.17
#교점에 별 만들기

def solution(line):
    dots = set()
    mx1, my1, mx2, my2 = -1000, -1000, 1000, 1000
    for i in range(len(line)):
        for j in range(i, len(line)):
            tmp = line[i][0]*line[j][1]-line[i][1]*line[j][0]
            if tmp != 0:
                x = (line[i][1]*line[j][2]-line[i][2]*line[j][1])/tmp
                y = (line[i][2]*line[j][0]-line[i][0]*line[j][2])/tmp
                if x==int(x) and y==int(y):
                    dots.add((int(x), int(y)))
                    mx1, my1, mx2, my2 = max(mx1, int(x)), max(my1, int(y)), min(mx2, int(x)), min(my2, int(y))
    answer = [["." for _ in range(mx1-mx2+1)] for _ in range(my1-my2+1)]
    for x, y in dots:
        answer[my1-y][x-mx2] = "*"
    return ["".join(x) for x in answer]