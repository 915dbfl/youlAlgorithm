#22.05.14
#큰 수 만들기

# 내 풀이(시간 초과)
def solution(number, k):
    l = len(number)-k
    number = list(number)
    cnt = 0
    while cnt < k:
        for i in range(len(number)-1):
            if int(number[i])<int(number[i+1]):
                del(number[i])
                cnt += 1
                break
        else:
            break

    return ''.join(number[:l])