# 22.09.23
# 단어 정렬
# 집합
# class2_1

import sys

N = int(sys.stdin.readline())
words = set()

for i in range(N):
  words.add(sys.stdin.readline().rstrip())

words = list(words)

for w in sorted(words, key = lambda x: (len(x), x)):
  print(w)