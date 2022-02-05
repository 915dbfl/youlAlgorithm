#21.10.18
import sys
def getCount(x, y, num):
  global colors, count
  chk = colors[x][y]
  for i in range(x, x+num):
    for j in range(y, y+num):
      if(chk != colors[i][j]):
        size = num//2
        getCount(x, y, size)
        getCount(x+size, y, size)
        getCount(x, y+size, size)
        getCount(x+size, y+size, size)
        return
  count[chk] += 1
  return

n = int(input())
colors = []
count = [0, 0]
for i in range(n):
  colors.append(list(map(int, sys.stdin.readline().rstrip().split())))
getCount(0, 0, n)
print(count[0])
print(count[1])