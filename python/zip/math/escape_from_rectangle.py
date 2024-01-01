# 22.09.23
# 직사각형에서 탈출
# calss2_1

import sys

x, y, w, h = map(int, sys.stdin.readline().split())

tmp1 = min(x, w-x)
tmp2 = min(y, h-y)

print(min(tmp1, tmp2))