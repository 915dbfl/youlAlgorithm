#22.06.13
#다단계 칫솔

#내 풀이
def solution(enroll, referral, seller, amount):
    answer = dict()
    for i in enroll:
        answer[i] = []
    for i in range(len(seller)):
        answer[seller[i]].append(amount[i]*100)
    for i in range(-1, -len(enroll)-1, -1):
        for j in range(len(answer[enroll[i]])):
            val = answer[enroll[i]][j]
            ancestor = referral[i]
            if int(val*0.1) >= 1:
                answer[enroll[i]][j] -= int(val*0.1)
                if ancestor != "-":
                    answer[ancestor].append(int(val*0.1))
    return list(map(sum, answer.values()))