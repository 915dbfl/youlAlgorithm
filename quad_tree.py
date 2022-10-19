#22.10.19
#쿼드트리
#class3/실버1
#divide and conquer

import sys

N = int(sys.stdin.readline())
tree = []

for _ in range(N):
  tree.append(sys.stdin.readline().rstrip())

def quad_tree(x, y, l):
  if l == 0:
    return str(tree[y][x])
  else:
    tmp = tree[y][x]
    for i in range(y, y+l):
      for j in range(x, x+l):
        if tmp != tree[i][j]:
          gap = l//2
          return "(" + quad_tree(x, y, gap) + quad_tree(x+gap, y, gap) + quad_tree(x, y+gap, gap) + quad_tree(x+gap, y+gap, gap) + ")"

    return str(tmp)

print(quad_tree(0, 0, N))
