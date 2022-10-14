#22.10.14
#나는야 포켓몬 마스터 이다솜
#class3/실버4
#dic

from collections import defaultdict
import sys

N, M = map(int, sys.stdin.readline().split())
dic_name = defaultdict(int)
dic_num = defaultdict(str)

for i in range(N):
  name = sys.stdin.readline().rstrip()
  dic_name[name] = i+1
  dic_num[i+1] = name

for i in range(M):
  q = sys.stdin.readline().rstrip()
  if q.isdigit():
    print(dic_num[int(q)])
  else:
    print(dic_name[q])