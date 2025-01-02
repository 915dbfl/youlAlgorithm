# 시간 초과

from itertools import combinations

my_cards = set()
amount = 0
max_round = 0

# 라운드 진행 함수
def round(rd, my_cards, cards, turn, coin):
    global max_round
    max_round = max(max_round, rd + 1)

    if len(cards) > turn:
        new_my_cards = set([cards[turn], cards[turn+1]])
        
        # 둘 중 하나 구매
        if coin >= 1:
            my_cards.add(cards[turn])
            coin -= 1
            pay(rd, my_cards, cards, turn, coin)
            my_cards.discard(cards[turn])
            coin += 1
            
            my_cards.add(cards[turn+1])
            coin -= 1
            pay(rd, my_cards, cards, turn, coin)
            my_cards.discard(cards[turn+1])
            coin += 1
            
        # 둘 다 구매
        if coin >= 2:
            my_cards |= new_my_cards
            coin -= 2
            pay(rd, my_cards, cards, turn, coin)
            my_cards -= new_my_cards
            coin += 2
            
        # 구매하지 않을 경우
        pay(rd, my_cards, cards, turn, coin)

# 합에 맞춰 카드를 제출하는 함수
def pay(rd, my_cards, cards, turn, coin):
    can_pay = False
    for case in combinations(my_cards, 2):
        if sum(case) == amount:
            can_pay = True
            my_cards -= set(case)
            round(rd + 1, my_cards, cards, turn + 2, coin)
            my_cards |= set(case)
    if not can_pay: return
    
def solution(coin, cards):
    global max_round, amount
    default = len(cards)//3
    amount = max(cards) + 1
    
    # 초기 카드 뽑기
    my_cards.add(cards[:default])

    # 라운드 진행
    round(0, my_cards, cards, default, coin)
    return max_round