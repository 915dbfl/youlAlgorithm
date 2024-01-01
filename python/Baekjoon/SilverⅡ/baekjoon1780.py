#21.01.24
#1780: 종이의 개수

import sys

def check(paper, l, x, y, s, e):
  key = paper[x][y]
  if l == 1:
    dic[key] += 1
    return
  else:
    for i in range(x, s):
      for j in range(y, e):
        if key != paper[i][j]:
          l //= 3
          for k in range(x, s, l):
            for m in range(y, e, l):
              check(paper, l, k, m, k+l, m+l)
          return
    dic[key] += 1
    return

N = int(sys.stdin.readline())
paper = []
dic = {-1: 0, 0: 0, 1: 0}

for _ in range(N):
  lst = list(map(int, sys.stdin.readline().split()))
  paper.append(lst)

check(paper, N, 0, 0, N, N)

print(f'{dic[-1]}\n{dic[0]}\n{dic[1]}')