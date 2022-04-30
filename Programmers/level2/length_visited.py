#22.04.30
#방문 길이

#내 풀이
def solution(dirs):
    answer = 0
    cur = (0, 0)
    order = {'U': [0, 1], 'D': [0, -1], 'R': [1, 0], 'L': [-1, 0]}
    dic = {}
    for dir in dirs:
        tmp = (cur[0]+order[dir][0], cur[1]+order[dir][1])
        if abs(tmp[0]) <= 5 and abs(tmp[1]) <= 5:
            if tmp not in dic.keys():
                dic[tmp] = [cur]
                if cur in dic.keys():
                    dic[cur].append(tmp)
                else:
                    dic[cur] = [tmp]
                answer += 1
            elif cur not in dic[tmp]:
                dic[tmp].append(cur)
                if cur in dic.keys():
                    dic[cur].append(tmp)
                else:
                    dic[cur] = [tmp]
                answer += 1
            cur = tmp
    return answer

#best 풀이: set 사용해 중복 거리 제거
def solution(dirs):
    cur = (0, 0)
    order = {'U': [0, 1], 'D': [0, -1], 'R': [1, 0], 'L': [-1, 0]}
    answer = set()
    for dir in dirs:
        x, y = cur[0]+order[dir][0], cur[1]+order[dir][1]
        if abs(x) <= 5 and abs(y) <= 5:
            answer.add((cur[0], cur[1], x, y))
            answer.add((x, y, cur[0], cur[1]))
            cur = (x, y)
    return len(answer)//2