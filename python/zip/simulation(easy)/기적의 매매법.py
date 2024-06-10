import sys
input = sys.stdin.readline

cash = int(input())
cost = list(map(int, input().split()))

jun = [cash, 0] # 현금, 구매한 주식 수
sung = [cash, 0]

# bnp 방식 구하기
for i in range(14):
    c = cost[i]
    # 주식을 구매할 현금이 없을 경우
    if jun[0] == 0:
        break
    # 주식 구매가 가능할 경우
    if jun[0] >= c:
        # 가능한 최대 주식 수를 구매
        cnt = jun[0] // c
        jun[0] -= cnt * c
        jun[1] += cnt

# timing 방식
# up, down 누적합 구하기
down = [1] * 14
up = [1] * 14
for i in range(1, 14):
    if cost[i-1] < cost[i]:
        up[i] = up[i-1] + 1
    if cost[i-1] > cost[i]:
        down[i] = down[i-1] + 1

for i in range(2, 14):
    c = cost[i]
    # 전량 매수 진행
    if down[i] >= 4 and sung[0] >= 0:
        cnt = sung[0] // c
        sung[0] -= cnt * c
        sung[1] += cnt
    if up[i] >= 4 and sung[1] > 0:
        sung[0] += c * sung[1]
        sung[1] = 0

sung_cost = sung[0] + sung[1] * cost[-1]
jun_cost = jun[0] + jun[1] * cost[-1]
if sung_cost > jun_cost:
    print("TIMING")
elif sung_cost < jun_cost:
    print("BNP")
else:
    print("SAMESAME")