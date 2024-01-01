#22.07.28
#섬 연결하기

#프림 알고리즘
def solution(n, costs):
    costs.sort(key = lambda x: x[2])
    tmp = costs.pop(0)
    answer = tmp[2]
    connected = [0 for _ in range(n)]
    connected[tmp[0]] = 1
    connected[tmp[1]] = 1

    while 0 in connected:
        for i in range(len(costs)):
            if connected[costs[i][0]] + connected[costs[i][1]] == 1:
                s, e, c = costs.pop(i)
                break
        answer += c
        if connected[s] == 1:
            connected[e] = 1
        else:
            connected[s] = 1
    return answer
