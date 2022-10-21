#22.10.21
#색종이 만들기
#class3/실버2
#divide and conquer

import sys
input = sys.stdin.readline

n = int(input())
paper = []

for i in range(n):
  paper.append(list(map(int, input().split())))

color = [0, 0]

def split_paper(x, y, l):
  if l == 1:
    color[paper[x][y]] += 1
  else:
    s = paper[x][y]

    for i in range(x, x+l):
      for j in range(y, y+l):
        if paper[i][j] != s:
          tmp = l//2
          split_paper(x, y, tmp)
          split_paper(x, y+tmp, tmp)
          split_paper(x+tmp, y, tmp)
          split_paper(x+tmp, y+tmp, tmp)
          return
    color[s] += 1

split_paper(0, 0, n)

print(color[0])
print(color[1])