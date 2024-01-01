#택배 배달과 수거하기
#그리디

# 탐욕기법
def solution(cap, n, deliveries, pickups):
    result = 0
    while deliveries or pickups:
        deliveries_cap, pickups_cap = cap, cap
        while deliveries and deliveries[-1] == 0:
            deliveries.pop()
        while pickups and pickups[-1] == 0:
            pickups.pop()
            
        result += 2*max(len(deliveries), len(pickups))
        
        
        while deliveries and deliveries_cap > 0:
            tmp = deliveries.pop()
            if tmp > deliveries_cap:
                deliveries.append(tmp - deliveries_cap)
                break
            else:
                deliveries_cap -= tmp
        while pickups and pickups_cap > 0:
            tmp = pickups.pop()
            if tmp > pickups_cap:
                pickups.append(tmp - pickups_cap)
                break
            else:
                pickups_cap -= tmp
                
    return result
                