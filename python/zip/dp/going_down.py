#22.12.03
#내려가기
#class4/골드5
#dp(공간 고려)

import sys

def getDP():
  max_dp = [[0, 0, 0], [0, 0, 0]]
  min_dp = [[0, 0, 0], [0, 0, 0]]
  max_dp[0] = lst[0]
  min_dp[0] = lst[0]

  for i in range(1, n):
    max_dp[1][0] = lst[i][0] + max(max_dp[0][0], max_dp[0][1])
    min_dp[1][0] = lst[i][0] + min(min_dp[0][0], min_dp[0][1])

    max_dp[1][1] = lst[i][1] + max(max_dp[0])
    min_dp[1][1] = lst[i][1] + min(min_dp[0])

    max_dp[1][2] = lst[i][2] + max(max_dp[0][2], max_dp[0][1])
    min_dp[1][2] = lst[i][2] + min(min_dp[0][2], min_dp[0][1])

    max_dp[0] = [max_dp[1][0], max_dp[1][1], max_dp[1][2]]
    min_dp[0] = [min_dp[1][0], min_dp[1][1], min_dp[1][2]]

  print(max(max_dp[1]), min(min_dp[1]))

n = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

getDP()

# 리팩토링
# 입력 데이터를 모두 읽어들일 경우 메모리 부족을 피할 수 없다.
import sys

n = int(sys.stdin.readline())
max_dp = [[0, 0, 0], [0, 0, 0]]
min_dp = [[0, 0, 0], [0, 0, 0]]

tmp = list(map(int, sys.stdin.readline().split()))
max_dp[0] = tmp
min_dp[0] = tmp

for _ in range(n-1):
  lst = list(map(int, sys.stdin.readline().split()))

  max_dp[1][0] = lst[0] + max(max_dp[0][0], max_dp[0][1])
  min_dp[1][0] = lst[0] + min(min_dp[0][0], min_dp[0][1])

  max_dp[1][1] = lst[1] + max(max_dp[0])
  min_dp[1][1] = lst[1] + min(min_dp[0])

  max_dp[1][2] = lst[2] + max(max_dp[0][2], max_dp[0][1])
  min_dp[1][2] = lst[2] + min(min_dp[0][2], min_dp[0][1])
  
  max_dp[0] = [max_dp[1][0], max_dp[1][1], max_dp[1][2]]
  min_dp[0] = [min_dp[1][0], min_dp[1][1], min_dp[1][2]]

print(max(max_dp[0]), min(min_dp[0]))