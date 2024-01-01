#22.11.02
#파도반 수열
#class3/실버3
#dp

import sys

t = int(sys.stdin.readline())
sequence = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for _ in range(t):
  n = int(sys.stdin.readline())

  for _ in range(11, n+1):
    sequence.append(sequence[-1]+sequence[-5])

  print(sequence[n])