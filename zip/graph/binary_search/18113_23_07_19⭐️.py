#그르다 김가놈
#이분탐색
#반복되는 작업이 존재하므로 pypy3 사용!

import sys
#김밥 개수, 꼬다리 길이, 김밥조각 최소 개수
n, k, m = map(int, input().split())

#꼬다리를 자르는 작업
lens = []
for _ in range(n):
    tmp = int(sys.stdin.readline())
    if tmp < k * 2 and tmp - k > 0:
        lens.append(tmp-k)
    elif tmp > k * 2:
        lens.append(tmp-k*2)

if len(lens) == 0:
    print(-1)
    exit(0)

# 이분탐색
p = -1
s, e = 1, max(lens)

while s <= e:
    mid = (s + e)//2
    total = sum([i//mid for i in lens])

    if total < m:
        e = mid-1
    
    else:
        p = mid
        s = mid+1
print(p)