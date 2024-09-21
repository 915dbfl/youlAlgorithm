# 사람 수가 1,000,000,000이므로 o(m) 불가능
# 이분 탐색을 통해 가능한 총 시간을 구한다.
# log(10^18) = 9

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
durs = [int(input()) for _ in range(n)]

l, r = min(durs), max(durs) * m
ans = r

while l <= r:
    mid = (l + r) // 2
    midAns = 0

    for dur in durs:
        midAns += mid // dur

    if midAns >= m:
        r = mid - 1
        ans = min(ans, mid)
    else:
        l = mid + 1

print(ans)