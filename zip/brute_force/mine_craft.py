#22.10.05
#마인크래프트
#class2/실버2
#브루트포스

from collections import Counter
import sys

n, m, inv = map(int, sys.stdin.readline().split())
ground = []

for _ in range(n):
  ground += map(int, sys.stdin.readline().split())

_sum = sum(ground)
h_min = min(ground)
h_max = max(ground)
ground = dict(Counter(ground))

time, height = 0, 0

for h in range(h_min, h_max+1):
  if _sum + inv >= n*m*h:
    t = 0
    for key in ground:
      if h < key:
        t += 2*ground[key]*(key-h)
      elif h > key:
        t += ground[key]*(h-key)
    if t <= time or time == 0:
      time = t
      height = h

print(time, height)