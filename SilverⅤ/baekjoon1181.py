#21.08.15
import sys
num = int(input())
words = set()
for i in range(num):
  words.add(str(sys.stdin.readline().strip()))
len_words = sorted(words, key=lambda l: (len(l), ord(l[0])))
for k in range(1, len(len_words)):
  a = len_words[k]
  for j in range(k-1, 0, -1):
    b = len_words[j]
    if len(len_words[k]) == len(len_words[j]):
      for i in range(0,len(a)):
        if a[i] != b[i]:
          if ord(a[i]) < ord(b[i]):
            len_words[k] = b
            len_words[j] = a
            k = j
            break
          else:
            break
    else:
      break
for i in len_words:
  sys.stdout.write(i+'\n')