# 케이크를 잘라 10을 많이 만들어야 함
# 10의 배수에 가까운 순서대로 자름
# 단, 20일 경우 한 번에 10이 두개가 생김
# 따라서 크기가 작은 순서대로 추가 정렬 필요
# greedy

n, m = map(int, input().split())
rolls = list(map(int, input().split()))

rolls = sorted(rolls, key = lambda x: (x%10, x))

cnt = 0
for peice in rolls:

    while(m > 0 and peice > 10):
        peice -= 10
        cnt += 1
        m -= 1

    if (peice == 10):
        cnt += 1

    if m < 1:
        break

print(cnt)

# 다른 풀이
n, m = map(int, input().split())
rolls = list(map(int, input().split()))

rolls = sorted(rolls, key = lambda x: (x%10, x))

cnt = 0
for peice in rolls:
    
    if peice >= 10 and peice % 10 == 0:
        cutCnt = min(peice // 10 - 1, m)
        cnt += cutCnt
        m -= cutCnt

        if peice == (10 * cutCnt) + 10:
            cnt += 1
    elif peice >= 10 and peice % 10 != 0:
        cutCnt = min(peice // 10, m)
        cnt += cutCnt
        m -= cutCnt

    if m < 1:
        break

print(cnt)