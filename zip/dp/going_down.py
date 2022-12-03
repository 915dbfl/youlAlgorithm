#22.12.03
#내려가기
#class4/골드5
#dp

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

# 얕은 복사/깊은 복사 개념 알아보기
# 값을 받자마자 바로 처리하는 풀이 학습하기