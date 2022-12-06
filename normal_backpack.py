#22.12.06
#평범한 배낭
#class4/골드5

#브루트포스, 백트래킹: 시간초과
import sys
sys.setrecursionlimit(10**6)

def fillBackpack(cur, weight, value):
  global ans
  for i in range(cur+1, len(lst)):
    if weight + lst[i][0] > k and ans < value:
      ans = value
      return
    else:
      fillBackpack(i, weight+lst[i][0], value+lst[i][1])
      fillBackpack(i, weight, value)

  if cur == len(lst)-1 and ans < value:
    ans = value

n, k = map(int, sys.stdin.readline().split())
lst = []

for _ in range(n):
  w, v = map(int, sys.stdin.readline().split())
  lst.append([w, v])

lst.sort(key = lambda x: [x[0], -x[1]])
ans = 0
fillBackpack(-1, 0, 0)
print(ans)