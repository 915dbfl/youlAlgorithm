#21.09.19
import sys
num= int(input())
dtable = []
ptable = []
dp = []
for i in range(num):
  day, pay = map(int, sys.stdin.readline().rstrip().split())
  dtable.append(day)
  ptable.append(pay)
  dp.append(pay)
dp.append(0)

for j in range(num-1, -1, -1):
  if j + dtable[j] > num:
    dp[j] = dp[j+1]
  else:
    dp[j] = max(dp[j+1], ptable[j] + dp[j + dtable[j]])
print(dp[0])