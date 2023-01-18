#23.01.18
#가장 긴 바이오토닉 부분 수열
#골드 4

import sys
n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))

up_dp = [1] * n
down_dp = [1] * n
answer = 1

for i in range(1, n):
  for j in range(i):
    if sequence[i] > sequence[j]:
      # up_dp[i] = max(up_dp[i], up_dp[j]+1)
      if up_dp[i] < up_dp[j] + 1:
        up_dp[i] = up_dp[j] + 1

for i in range(2, n+1):
  for j in range(1, i):
    if sequence[-i] > sequence[-j]:
      # down_dp[-i] = max(down_dp[-i], down_dp[-j]+1)
      if down_dp[-i] < down_dp[-j] + 1:
        down_dp[-i] = down_dp[-j] + 1
  up_dp[n-i] += down_dp[-i]-1

print(max(up_dp))