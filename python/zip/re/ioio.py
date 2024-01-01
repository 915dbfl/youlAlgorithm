#22.10.25
#IOIO
#class3/실버1

import re

n = int(input())
m = int(input())
s = input().rstrip()
cnt = 0

for case in re.findall('I(?:OI)+', s):
  c = case.count("O")

  if c >= n:
    cnt += c-n+1
print(cnt)