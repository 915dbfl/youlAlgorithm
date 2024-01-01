#22.11.07
#비밀번호 찾기
#class3/실버4
#hash

import sys

n, m = map(int,sys.stdin.readline().split())

sites = dict()

for _ in range(n):
  url, pwd = sys.stdin.readline().split()
  sites[url] = pwd

for _ in range(m):
  q = sys.stdin.readline().rstrip()
  print(sites[q])



