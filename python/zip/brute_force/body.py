#22.10.03
#덩치
#class2/실버5
#brute_force
#해당 방식이 dp가 아닌 이유는 반복되는 작은 문제들이 없기 때문이다. 단순이 자신보다 작은 모든 경우를 파악한 후 등수를 매기는 방식이다!

import sys

N = int(sys.stdin.readline())
lst = []
rank = [1 for _ in range(N)]

for i in range(N):
  lst.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N):
  for j in range(i-1, -1, -1):
    if lst[i][0] > lst[j][0] and lst[i][1] > lst[j][1]:
      rank[j] += 1
    elif lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
      rank[i] += 1

print(" ".join(list(map(str, rank))))