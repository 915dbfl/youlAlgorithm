# 기타리스트

#재귀: 시간초과 2 ** 50
import sys
n, s, m = map(int, input().split())
volumes = list(map(int, input().split()))

Max = 0
def getVolume(i, volume):
    global Max
    if i == n:
        Max = max(Max, volume)
        return

    maxVolume = volume + volumes[i]
    minVolume = volume - volumes[i]

    if minVolume < 0 and maxVolume > m:
        return

    # 볼륨 증가
    if maxVolume <= m:
        getVolume(i+1, maxVolume)
    # 볼륨 감소
    if minVolume >= 0:
        getVolume(i+1, minVolume)
        
getVolume(0, s)
if Max == 0:
    print(-1)
else:
    print(Max)


# dp: 오답
import sys
n, s, m = map(int, input().split())
volumes = list(map(int, input().split()))

dp = [0]*n
for i in range(n):
    if i == 0:
        if volumes[i] + s <= m:
            dp[i] = volumes[i] + s
        elif volumes[i] - s >= 0:
            dp[i] = s - volumes[i]
        else:
            print(-1)
            exit(0)
    else:
        tmp1 = volumes[i] + dp[i-1]
        tmp2 = volumes[i] + (dp[i-1]-volumes[i-1]*2)
        tmp3 = dp[i-1] - volumes[i]

        tmps = []
        if 0 <= tmp1 <= m:
            tmps.append(tmp1)
        if dp[i-1] - volumes[i-1] >= 0 and 0 <= tmp2 <= m:
            tmps.append(tmp2)
        if 0 <= tmp3 <= m:
            tmps.append(tmp3)
        
        if len(tmps) == 0:
            print(-1)
            break

        dp[i] = max(tmps)
else:
    print(dp[-1])                                                                     

# dp 다른 방식
n, s, m = map(int, input().split())
volumes = list(map(int, input().split()))
dp = [[0] * (m+1) for _ in range(n+1)]
dp[0][s] = 1

for i in range(n):
    for j in range(m+1):
        if dp[i][j] == 1:
            if j+volumes[i] <= m:
                dp[i+1][j+volumes[i]] = 1
            if j-volumes[i] >= 0:
                dp[i+1][j-volumes[i]] = 1

for i in range(m, -1, -1):
    if dp[n][i]==1:
        print(i)
        break
else:
    print(-1)