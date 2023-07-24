#조짜기
#dp

n = int(input())
lst = list(map(int, input().split()))
dp = [0]*n

for i in range(n):
    for j in range(i):
        if j == 0:
            dp[i] = abs(max(lst[:i+1]) - min(lst[:i+1]))
        else:
            dp[i] = max(dp[i], dp[j] + abs(max(lst[j+1:i+1]) - min(lst[j+1:i+1])))

print(dp[-1])