# 2022.09.23
# 체스판 다시 칠하기
# class2/실버4
# 브루트 포스

# "wb"로 시작하는 경우와 "bw"로 시작하는 경우를 나눠 더 적게 변경되는 경우를 모아 가장 작은 값을 반환한다.

import sys

h, w = map(int, sys.stdin.readline().split())
board = []
count = []

for i in range(h):
  board.append(sys.stdin.readline().rstrip())

for i in range(h-8+1):
  for j in range(w-8+1):
    type1, type2 = 0, 0
    for a in range(i, i+8):
      for b in range(j, j+8):
        if (a+b)%2 == 0:
          if board[a][b] != "W":
            type1 += 1
          elif board[a][b] != "B":
            type2 += 1
        else:
          if board[a][b] != "B":
            type1 += 1
          elif board[a][b] != "W":
            type2 += 1
    count.append(min(type1, type2))

print(min(count))
    