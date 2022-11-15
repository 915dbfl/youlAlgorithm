#22.11.14
#거짓말
#class4/골드4
#bfs, dfs
#union-find(분리집합)

#bfs
import sys
from collections import defaultdict, deque

def bfs(): #진실을 말해야 하는 사람 모두 구하기
  dq = deque(truth)
  
  for p in truth:
    visited[p-1] = 1
  
  while dq:
    tmp = dq.popleft()

    for p in dic[tmp]:
      if visited[p-1] == 0:
        visited[p-1] = 1
        dq.append(p)
        truth.add(p)

n, m = map(int, sys.stdin.readline().split())

num, *truth = list(map(int, sys.stdin.readline().split()))
truth = set(truth)
cnt = 0
party = []
dic = defaultdict(set)
visited = [0] * n

for _ in range(m): # 파티 정보 받아오기
  n, *lst = list(map(int, sys.stdin.readline().split()))
  lst = set(lst)
  party.append(lst)

  for c in lst:
    for p in lst:
      if c != p :
        dic[c].add(p)

bfs()
if num == 0:
  print(m)
else:
  for p in party: # 과장을 말할 수 있는 파티 count
    for t in truth:
      if t in p:
        break
    else:
      cnt += 1

  print(cnt)

#합집합
import sys

def getKnows(m):
  global know
  for _ in range(m): # 매 파티마다 진실을 알게 되는 사람이 생길 수 있기 때문에 파티수 만큼 반복
      for p in parties:
          if know & p:
              know |= p

n, m = map(int, sys.stdin.readline().split())

num, *know = list(map(int, sys.stdin.readline().split()))
know = set(know)
cnt = 0
parties = []

for _ in range(m): # 파티 정보 받아오기
  n, *lst = list(map(int, sys.stdin.readline().split()))
  lst = set(lst)
  parties.append(lst)

if num == 0:
  print(m)
else:
  getKnows(m) #진실을 말해야 하는 사람 모두 구하기

  for party in parties: # 과장을 말할 수 있는 파티 count
    if know & party:
      continue
    cnt += 1

  print(cnt)

  #union-find 알고리즘: https://c4u-rdav.tistory.com/44