#2022.04.26
#이진 변환 반복하기

#내 풀이
def solution(s):
    rmv, cnt = 0, 0
    while s != "1":
        cnt += 1
        rmv += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]
    return [cnt, rmv]

#best 풀이 : 제거할 0이 아닌 1에 초점을 둔 풀이!
def solution(s):
    rmv, cnt = 0, 0
    while s != "1":
        cnt += 1
        tmp = s.count("1")
        rmv += len(s) - tmp
        s = bin(tmp)[2:]
    return [cnt, rmv]