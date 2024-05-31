# 1시간
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = [0] + list(map(int, input().split()))

# 누적합 구하기
for i in range(1, n+1):
    s[i] += s[i-1]

# 투포인터 활용
if sum(s) <= k:
    print(0)
else:
    p1, p2 = 0, 1
    sumL = [0] * (n+1)
    
    while p2 <= n:

        # p2 위치 구하기
        while 1:
            # p2가 범위를 벗어나거나 p2 ~ p1 사이 합이 k 이상일 경우
            if p2 > n or (s[p2] - s[p1] >= k):
                break
            # p2값 p2-1의 값으로 초기화
            sumL[p2] = max(sumL[p2-1], sumL[p2])
            p2 += 1
            
        # p2 범위가 벗어났다면 반복문에서 나감
        if p2 > n:
            break
        
        # p2값 업데이트
        sumL[p2] = max(sumL[p2], sumL[p1] + (s[p2] - s[p1] - k))

        # p1 업데이트
        p1 += 1

    print(sumL[-1])