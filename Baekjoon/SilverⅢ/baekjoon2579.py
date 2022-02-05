#21.10.12
import sys
N = int(input())
score = [0, 0]
dp = [0, 0]
for i in range(N):
  score.append(int(sys.stdin.readline().rstrip()))
dp.append(score[2])

for i in range(3, N+2):
  temp1 = score[i] + dp[i-2]
  temp2 = score[i] + score[i-1] + dp[i-3]
  dp.append(max(temp1, temp2))

print(dp)