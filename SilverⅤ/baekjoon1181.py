#21.08.16
num = int(input())
words = set()
for i in range(num):
  words.add(input())
words = list(words)
words.sort(key = lambda word: (len(word), word))
for i in words:
  print(i)