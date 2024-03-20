#브루트 포스
from itertools import product

def solution(users, emoticons):
    subscribers, sales = 0, 0 # 가입자 수, 매출액
    
    # 결과 업데이트
    def updateResult(sb, tt):
        nonlocal subscribers, sales
        # 구독자가 더 많다면
        if subscribers < sb:
            subscribers = sb
            sales = tt
        # 구독자는 같지만 매출액이 더 크다면
        elif subscribers == sb and sales < tt:
            sales = tt
    
    def checkSubscriber(case):
        case_sub = 0
        case_sale = 0
        user_cost = [0] * len(users)
        
        price = []
        for i in range(len(case)):
            price.append(emoticons[i] * ((100-case[i])/100))
            
        # 각 유저 비용 계산
        for i in range(len(users)):
            for j in range(len(price)):
                # 원하는 할인율보다 많이 할인할 경우
                if users[i][0] <= case[j]:
                    user_cost[i] += price[j]
            
            # 예산 초과 확인
            if users[i][1] <= user_cost[i]:
                user_cost[i] = 0
                case_sub += 1

        # 판매액 합계
        case_sale = sum(user_cost)
        updateResult(case_sub, case_sale)
        
    percent = [10, 20, 30, 40]
    for case in product(percent, repeat = len(emoticons)):
        checkSubscriber(case)
        
    return [subscribers, sales]