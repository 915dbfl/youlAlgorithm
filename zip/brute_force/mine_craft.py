#22.10.05
#마인크래프트
#class2/실버2
#브루트포스

from collections import Counter
import sys

n, m, b = map(int, sys.stdin.readline().split())
ground = []

for i in range(n):
  ground += list(map(int, sys.stdin.readline().split()))

counter = Counter(ground).most_common()

if len(counter) == 1:
  print(0, counter[0][0])
else:
  answer = [n*m*2*256, 0]

  for i in range(max(ground), min(ground)-1, -1):
    s = 0
    inventory = b
    m, r = 0, 0
    for v, c in counter:
      if i < v:
        s += 2*c*(v-i)
        m += c*(v-i)
      elif i > v:
        s += c*(i-v)
        r += c*(i-v)
    if inventory + m - r >= 0 and s < answer[0]:
      answer = [s, i]

  print(answer[0], answer[1])