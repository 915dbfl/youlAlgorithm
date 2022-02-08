#22.02.08
#키패드 누르기(수정)

def solution(numbers, hand):
    answer = ''
    dis = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    left = [3, 0]
    right = [3, 2]
    
    for i in numbers:
        if i % 3 == 1:
            answer += 'L'
            left = dis[i]
        elif i % 3 == 0 and i != 0:
            answer += 'R'
            right = dis[i]
        else:
            l = abs(left[0] - dis[i][0]) + abs(left[1] - dis[i][1])
            r = abs(right[0] - dis[i][0]) + abs(right[1] - dis[i][1])
            
            if l < r:
                answer += 'L'
                left = dis[i]
            elif r < l:
                answer += 'R'
                right = dis[i]
            else:
                answer += hand[0].upper()
                if hand[0] == 'r':
                    right = dis[i]
                else:
                    left = dis[i]
    
    return answer