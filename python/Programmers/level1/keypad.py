#22.02.07
#키패드 누르기

def getDis(s, e):
    cnt = 0
    tmp = abs(s-e)
    
    while tmp > 0:
        if tmp >= 3:
            cnt += 1
            tmp -= 3
        else:
            cnt += tmp
            break
    return cnt


def solution(numbers, hand):
    answer = ''
    lct = {'left': 10, 'right': 12}
    
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            lct['left'] = i
        elif i in [3, 6, 9]:
            answer += 'R'
            lct['right'] = i
        else:
            tmp = 11 if i == 0 else i
            lft = getDis(lct['left'], tmp)
            rht = getDis(lct['right'], tmp)
            if lft < rht:
                answer += 'L'
                lct['left'] = tmp
            elif lft > rht:
                answer += 'R'
                lct['right'] = tmp
            else:
                answer += hand[0].upper()
                lct[hand] = tmp
    
    print(answer)

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")