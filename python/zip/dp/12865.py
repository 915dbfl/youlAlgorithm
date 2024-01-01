# 평범한 배낭

# 잘못된 풀이 - 같은 짐을 여러 번 선택할 수 없다는 것을 처리하지 않음
n, k = map(int, input().split())
dp = [0] * (k+1) # dp[i]는 무게 i일 때 가능한 최대 v
packs = [] # pack에 대한 정보 모두 저장
for i in range(n):
    w, v = map(int, input().split())
    packs.append([w, v])
    dp[w] = max(dp[w], v)
print(dp)

for pw, pv in packs:
    for c in range(pw+1, k+1):
        dp[c] = max(dp[c], dp[c-pw] + pv)
    print(pw, dp)

# 다른 풀이
# dp[i][j]는 i번째 물건까지 넣었을 때 j의 무게일 떄 최대 가치
n, k = map(int, input().split())
stuff = [[0, 0]]
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(n):
    stuff.append(list(map(int, input().split())))

for i in range(1, n+1):
    w, v = stuff[i]
    for j in range(1, k+1):
        if w > j: # 넣는 총 무게보다 w가 클 경우
            dp[i][j] = dp[i-1][j] # 해당 물건을 포함 안 했을 때 최대 v값으로 넣음
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[-1][-1])