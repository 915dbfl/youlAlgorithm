#22.09.26
#단어정렬
#class2/silver5
#정렬

import sys

N = int(sys.stdin.readline())
words = set()

for i in range(N):
  words.add(sys.stdin.readline().rstrip())

answer = sorted(list(words), key = lambda x: (len(x), x))

for i in answer:
  sys.stdout.write(i + "\n")