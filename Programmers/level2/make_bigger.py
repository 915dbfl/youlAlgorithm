#22.04.14
#큰 수 만들기

#내 풀이(오답)
def solution(number, k):
    cnt = 0
    idx = 0
    chk = False
    while cnt < k:
        if idx == len(number)-1:
            if chk == False:
                return number[:len(number) - (k-cnt)]
            else:
                idx = 0
                chk = False
        if int(number[idx]) < int(number[idx+1]):
            number = number[:idx] + number[idx+1:]
            cnt += 1
            chk = True
        else:
            idx += 1
    return number