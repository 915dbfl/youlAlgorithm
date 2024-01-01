#22.06.19
#[3차] 압축

#내 풀이
import re

def solution(msg):
    dic = dict()
    answer = []
    num = 27
    while msg:
        keys = sorted(dic.keys(), key = lambda x: len(x), reverse = True)
        for i in keys:
            result = re.match(r"%s+" % i, msg)
            if result != None:
                answer.append(dic[i])
                if len(msg) > len(i):
                    msg = msg[len(i):]
                    dic[i+msg[0]] = num
                    num += 1
                else:
                    msg = ""
                break
        else:
            answer.append(ord(msg[0])-64)
            if len(msg) == 1:
                msg = ""
            else:
                dic[msg[:2]] = num
                msg = msg[1:]
                num += 1
    return answer


#best 풀이
def solution(msg):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dic = {k:v for (k,v) in zip(alpha, list(range(1,27)))}
    answer = []

    while True:
        if msg in dic:
            answer.append(dic[msg])
            break
        for i in range(1, len(msg)+1):
            if msg[:i] not in dic:
                answer.append(dic[msg[0:i-1]])
                dic[msg[:i]] = len(dic)+1
                msg = msg[i-1:]
                break

    return answer