#22.07.06
#거리두기 확인하기

def checkRule(place):
    for i, row in enumerate(place):
        if "PP" in row or "POP" in row:
            return 0
        if i != 0:
            for j, p in enumerate(row):
                if p == "P":
                    if place[i-1][j] == "P":
                        print(place, row, j, "P")
                        return 0
                    elif place[i-1][j] == "O":
                        if j != 0 and place[i-1][j-1] == "P":
                            return 0
                        if j != 4 and place[i-1][j+1] == "P":
                            return 0
                        if i >= 2 and place[i-2][j] == "P":
                            return 0
                    elif place[i-1][j] == "X":
                            if j != 0 and place[i-1][j-1] == "P" and place[i][j-1] == "O":
                                return 0
                            if j != 4 and place[i-1][j+1] == "P" and place[i][j+1] == "O":
                                return 0
    return 1
        

def solution(places):
    global answer
    answer = []
    for place in places:
        answer.append(checkRule(place))
    return answer