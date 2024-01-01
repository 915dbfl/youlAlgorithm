#동전 2

#시간초과
import sys

n, k = map(int, input().split())
w = []

for _ in range(n):
    w.append(int(sys.stdin.readline()))
w.sort(reverse=True)
mcount = 10000

def temp(cur, left, count):
    global mcount
    if(left == 0):
        mcount = min(mcount, count)
        return
    
    if(cur >= len(w)) or (left < 0) or count > mcount:
        return
    
    tmp = left // w[cur]
    for i in range(tmp,-1,-1):
        temp(cur+1, left - (w[cur]*i), count+i)

temp(0, k, 0)
if mcount == 10000:
    print(-1)
else:
    print(mcount)

#dp⭐️
#초기값을 10000이 아닌 10001로 해야 하는 이유
#10000으로 초기화할 경우, dp[-1]이 10000인 경우는 최소값을 없는 경우가 아니라 10000인 경우일 수 있으므로 무조건 -1로 출력되면 안된다.
import sys
n, k = map(int, sys.stdin.readline().split())
coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline()))

#i일 때 dp[i]는 i의 가치를 만들기 위해 필요한 최소의 동전 개수 저장
dp = [10000] * (k+1)
dp[0] = 0
for i in range(n):
    for j in range(coin[i], k+1):
        dp[j] = min(dp[j], dp[j-coin[i]]+1)

if dp[-1] == 10000:
    print(-1)
else:
    print(dp[-1])