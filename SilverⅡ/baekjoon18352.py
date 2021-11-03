#21.11.03
#다익스트라
#오답

import sys
# X로 시작해서 각 지점까지 갈 수 있는 최단 거리
def getLst():
  global X, K
  global M_dic, lst
  key = 0
  rng = 1
  order = [X]
  for i in range(K):
    for j in range(rng):
      check = order[key]
      temp = 0
      if check in M_dic.keys():
        for i in M_dic[check]:
          if i not in order:
            temp += 1
            order.append(i)
            lst[i] = lst[check] + 1
      key += 1
      rng = temp

N, M, K, X = map(int, sys.stdin.readline().split())
#최단 거리를 저장하는 리스트
lst = [M+1 for _ in range(N+1)]
lst[X] = 0

#단방향 도로 저장 딕셔너리
M_dic = {}
for j in range(M):
  temp1, temp2 = map(int, sys.stdin.readline().split())
  if temp1 not in M_dic.keys():
    M_dic[temp1] = []
  M_dic[temp1].append(temp2)

getLst()
if K in lst:
  for i in range(1, N+1):
    if lst[i] == K:
      print(i)
else:
  print(-1)