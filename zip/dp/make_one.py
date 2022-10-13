#22.10.13
#1로 만들기
#class3/실버3
#DP

#DP
N = int(input())
dp = [0, 0, 1, 1]

for i in range(4, N+1):
  if i % 3 == 0 and i % 2 == 0:
    tmp = min(dp[i//3]+1, dp[i//2]+1)
    dp.append(min(tmp, dp[i-1]+1))
  elif i % 3 == 0:
    dp.append(min(dp[i//3]+1, dp[i-1]+1))
  elif i % 2 == 0:
    dp.append(min(dp[i//2]+1, dp[i-1]+1))
  else:
    dp.append(dp[i-1]+1)

print(dp[N])

#브루트 포스(시간초과)
def brute_force(i, cnt):
  if i == 1:
    answer.append(cnt)
    return
  if i % 3 == 0:
    brute_force(i//3, cnt+1)
  if i % 2 == 0:
    brute_force(i//2, cnt+1)
  brute_force(i-1, cnt+1)


N = int(input())
answer = []
brute_force(N, 0)
print(min(answer))