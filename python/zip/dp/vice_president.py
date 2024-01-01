#22.12.24
#부회장이 될테야
#알고리즘 스터디 1주차 -1
#dp277

import sys
input = sys.stdin.readline

t = int(input())

lst = [[i for i in range(15)]] # dp

for _ in range(t):
  k = int(input()) # 층
  n = int(input()) # 호

  if len(lst)-1 < k:
    for _ in range(k-len(lst)+1): # 추가 층 정보 구하기
      lst.append([0]*15)
      for i in range(1, 15):
        lst[-1][i] = lst[-1][i-1] + lst[-2][i]

  print(lst[k][n])