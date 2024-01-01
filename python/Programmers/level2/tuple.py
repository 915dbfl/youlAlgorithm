#2022.03.21
#튜플

#내 풀이
def solution(s):
    answer = []
    lst = list(s[2:len(s)-2].split("},{"))
    lst.sort(key = lambda x: len(x))
    for i in lst:
        i = list(i.split(","))
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
    return answer