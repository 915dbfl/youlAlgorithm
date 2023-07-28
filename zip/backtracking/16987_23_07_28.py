#계란으로 계란치기
#완전탐색

import sys
n = int(input())
wlst = []
dlst = []
breakC = [0] * n
mCount = 0

for _ in range(n):
    d, w = map(int, sys.stdin.readline().split())
    wlst.append(w)
    dlst.append(d)

def bruteForce(cur):
    global mCount
    if cur == n:
        mCount = max(mCount, sum(breakC))
        return
    
    # cur번째 계란이 깨지지 않은 경우만
    if breakC[cur] == 0:
        # 모든 경우 확인
        if sum(breakC) == n-1:
            bruteForce(cur+1)
        else:
            for i in range(n):
                # i번째 계란이 깨지지 않았을 경우
                if i != cur and breakC[i] == 0:
                    dlst[cur] -= wlst[i]
                    dlst[i] -= wlst[cur]

                    if dlst[cur] <= 0:
                        breakC[cur] = 1
                    if dlst[i] <= 0:
                        breakC[i] = 1
                    bruteForce(cur+1)
                    dlst[cur] += wlst[i]
                    dlst[i] += wlst[cur]
                    breakC[cur] = 0
                    breakC[i] = 0
    # 깨진 경우 다음 계란으로 이동
    else:
        bruteForce(cur+1)

bruteForce(0)
print(mCount)