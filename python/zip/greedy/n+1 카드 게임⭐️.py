"""
# 주요 정보
- 주어진 순서대로 카드를 뽑는다.
    - 시작할 때 n/3 장의 카드를 뽑는다.
    - 매라운드에서 2장의 카드를 뽑는다.
- 동전을 사용해 뽑은 카드를 가질 수 있다.

# 최대 라운드 수 출력
- 매 순간 최적의 선택을 한다.
    - 동전을 사용하지 않고 넘어갈 수 있는가?
    - 1개의 동전을 쓰고 넘어갈 수 있는가?
    - 2개의 동전을 써야 하는가 
    => 순서대로 확인
- 카드 구매는 단계에 국한되지 않고 진행한다.
    - 카드의 상태를 다음과 같이 세 개지로 구분한다.
    1. 내가 가지고 있는 카드
    2. 뽑은 카드
    3. 뽑기 전의 카드
"""

from collections import deque

def solution(coin, cards):             
    card_size = len(cards)
    pocket = set(cards[:card_size // 3])
    cards = deque(cards[card_size // 3:])
    pick_set = set()
    
    def can_remove(s1, s2):
        for num in list(s1):
            # 모든 것을 확인할 필요 없이 필요한 값이 있는지만 확인하면 됨
            if card_size + 1 - num in s2:
                s1.remove(num)
                s2.remove(card_size + 1 - num)
                return True
        return False
    
    round = 1
    while cards:
        pick_set.add(cards.popleft())
        pick_set.add(cards.popleft())
        
        if can_remove(pocket, pocket):
            round +=1
        elif coin >= 1 and can_remove(pocket, pick_set):
            coin -= 1
            round += 1
        elif coin >= 2 and can_remove(pick_set, pick_set):
            coin -= 2
            round += 1
        else:
            break
            
    return round