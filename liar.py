#22.11.14
#거짓말
#class4/골드4

import sys

def makeSearch(m): #진실을 말해야 하는 사람 모두 구하기
  global truth
  for i in range(m):
    if len(party[i] & truth) > 0:
      truth |= party[i]
      for j in range(i):
        if len(party[j] & truth) > 0:
          truth |= party[j]

n, m = map(int, sys.stdin.readline().split())

num, *truth = list(map(int, sys.stdin.readline().split()))
truth = set(truth)
cnt = 0
party = []

for _ in range(m): # 파티 정보 받아오기
  n, *lst = list(map(int, sys.stdin.readline().split()))
  lst = set(lst)
  party.append(lst)

if num == 0:
  print(m)
else:
  party.sort(key = lambda x: -len(x))

  makeSearch(m)
  print(truth)

  for p in party: # 과장을 말할 수 있는 파티 count
    if len(truth & p) == 0:
      cnt += 1

  print(cnt)

  # https://www.acmicpc.net/board/view/96247